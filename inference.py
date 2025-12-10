import argparse
import os
import re

## MAKE custom changes here ####
os.environ["CUDA_VISIBLE_DEVICES"]="0"
os.environ['TRANSFORMERS_CACHE'] = ''
os.environ['TOKENIZERS_PARALLELISM'] = "false"

import torch
from torch.optim import AdamW
from torch.utils.data import DataLoader
from peft import (
    get_peft_config,
    get_peft_model,
    get_peft_model_state_dict,
    set_peft_model_state_dict,
    LoraConfig,
    PeftType,
    PrefixTuningConfig,
    PromptEncoderConfig,
    prepare_model_for_kbit_training,
    PeftModel
)

from tqdm import tqdm
import evaluate
import pandas as pd
import numpy as np
from collections import Counter
from datasets import Dataset
from transformers import BitsAndBytesConfig, Trainer
from transformers import AutoModelForSequenceClassification, AutoTokenizer, get_linear_schedule_with_warmup, set_seed
from sklearn.metrics import f1_score, accuracy_score, classification_report
import bitsandbytes as bnb
import numpy as np

batch_size = 40
max_len = 512

peft_model_id = "model/Sauer-7b-emotion"

quant_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16,
    bnb_4bit_use_double_quant=True
)

config = LoraConfig.from_pretrained(peft_model_id)
model = AutoModelForSequenceClassification.from_pretrained('VAGOsolutions/SauerkrautLM-7b-HerO', 
                                                           return_dict=True, 
                                                           quantization_config=quant_config,
                                                           num_labels=6,
                                                           problem_type="multi_label_classification",
                                                           attn_implementation="flash_attention_2")


tokenizer = AutoTokenizer.from_pretrained('VAGOsolutions/SauerkrautLM-7b-HerO',
                                          padding_side="right")
tokenizer.pad_token_id = tokenizer.eos_token_id

model = PeftModel.from_pretrained(model, peft_model_id, device_map={"":0})
model.eval()

tokenizer.pad_token_id = tokenizer.eos_token_id
model.config.pad_token_id = tokenizer.pad_token_id
model.cuda()

def tokenize_function(examples):
    # max_length=None => use the model max length (it's actually the default)
    outputs = tokenizer(examples["Text"], truncation=True, max_length=max_len)
    return outputs

def collate_fn(examples):
    return tokenizer.pad(examples, padding="longest", return_tensors="pt")

def chunks(xs, n):
    n = max(1, n)
    return [xs[i:i+n] for i in range(0, len(xs), n)]

# add your own input strings here
inputs = ["""Der Kapitän nickte lächelnd. »Hofft nur von dem Anblick der Küste nicht zu viel Schönes,« warnte er. »Das meiste ist Busch!«
    Ein Grüßen herüber und hinüber, ein Hurra der Matrosen auf dem Dampfer, und die wissenschaftliche Expedition hatte in aller Form begonnen. Bisher war man nur in den Häfen zivilisierter Völker gewesen oder schwamm in bequemer, ja eleganter Kajütte über das Meer, hier aber, hinter der Ansiedelung Palma, in dem kleinen Dorfe
    Lepée, entfaltete sich das geheimnisvolle, unbekannte Naturleben der Neger, hier wohnten die Schwarzen, unbeeinflußt von Kultur und Sitte, ganz wie seit Anbeginn der Schöpfung, eben darum aber das Sehenswerteste, Interessanteste, was es für die jungen abenteuerlustigen Reisenden überhaupt geben konnte.
    Die Knaben sahen immer wieder nach ihren Gewehren.""",
          """Die edelscheuen Rosse, wie kühn sie auch ihre Brust den schönern Gefahren entgegenzuwerfen gewohnt waren, schnaubten hier wild vor häßlichen Klängen und Gestalten, warfen sich, selbst Ottos Lichtbrauner nicht ausgenommen, ohne Zaum und Schenkel zu achten, herum, und rissen ihre tapfern, zürnenden Reiter mit sich fort in ungezähmte, ungeordnete Flucht. Da heulten die Finnlandskrieger höhnend hintendrein, da schwirrten deren blitzesschnelle Geschosse nach, manch edlen Reitermann in Todesnacht aus dem Sattel reißend, da erlagen viel wackre normännische Fußknechte, vom Beistand ihrer Roßgeschwader verlassen, dem Grimme des siegenden Heidenvolks. Erst spät, in einem engen Tale, gelang es den beiden Hauptleuten, ihre eignen rasenden Rosse zu bändigen, und eine Schar ihrer Getreuen um sich her zum Stehen zu bringen.\n Da blitzte es auf einem Schneeberge vor ihnen auf, wie ein drehendes Feuerrad, und mitten drinne ward die Zauberjungfrau sichtbar, in furchtbarer Schöne, fliegend ihre langen, goldnen Locken, dräuend in der gehobnen Rechten ein blitzendes Schwert, aus der Linken emporwehend ein grünender Zweig, der eiskalten Jahreszeit zum Hohn. – »Kennt ihr mich nun?« rief sie zu den Rittern hinunter.""",
         """Wilhelmine.
 (aufspringend). Das überlebe ich nicht! Ach! 
       (Sie sinkt wieder auf ihren Stuhl nieder und weint laut mit Taschentuch vor dem Gesicht. Pingel steht bei ihr, macht verschiedene Gesten, die andeuten, daß er sie zu trösten sucht. Wilhelmine reagiert darauf. Er streichelt ihr das Haupt, sie läßt es sich gefallen, stummes Spiel der beiden, bis Pingel bald nachher sie küßt.)
 Bollmann. Arme Frauen! Es ist ein Bild zum Jammern!
 Jette. Ein Bild zum Jammern! Mich ist ooch dat Herz jeknickt!""",
                    """Die kleine Weckuhr zeigte fast sieben Uhr. Er trat an Marions Bett und schaute lange die Schlafende an. Schließlich beugte er sich nieder und küßte sie auf die Stirn.
   Sie erwachte. »Marion«, sagte er, ich muß gehen.""",
         """Justine (schwer athmend). Ja, Bruder – der Mensch hatte mich auch auf den Tod erschreckt.
 Sickingen. Der Mensch? Welcher Mensch?
 Justine. Ich kenn' ihn nicht – tritt mir Einer in den Weg – sah aus halb wie 'n Bauer, halb wie 'n Phantast – schaut' mir keck in's Gesicht, mit so dunkeln, rollenden Augen – es graute mir vor ihm – d'rauf wollt' er meine Hand erfassen – oder schien's mir nur so – kurz, mich überlief's wie Feuer, und ich rannt' fast athemlos dem Schloß zu.
 Sickingen. So erschreckt! Weil Einer Deine Hand erfaßt? 's ist sonst nicht Deine Art.
 Justine. Ich fürcht' mich nicht vor mein's Gleichen. 
 Aber ich sagte Dir's oft: Du kennst uns're Bauern nicht – und was sie für Reden führen! 
 Höre, Bruder! Wenn's in den Krieg geht, diesmal bleib' ich nicht daheim.""",
         """Zweiundzwanzigster Auftritt
 Die Vorigen.
 Es ist vollständig dunkel geworden. Die Szene wird nur vom flackernden Herdfeuer Schefakas erleuchtet. Das gibt gespenstige Bilder. Das Läuten der Gebetsbretter kommt näher. Es stellen sich Beter und Neugierige ein, die vom Scheik zum Schaffen von Sitzen angehalten werden. Ihren vereinten Kräften gelingt es auch, den schweren, sechstausend Jahre alten Thron umzudrehn, auf den sich Abu Kital zu setzen hat, das Gesicht zum Zelt gerichtet. Um diese Vorbereitungen zu beleben und anschaulicher zu machen, kommen die Nachbildungen des Scheiks, des Imams, des Kadis und Babels beliebig wieder aus dem Zelt, um irgend etwas zu besorgen oder nachzuholen. Es gerät für einige Augenblicke alles durcheinander, bis die Phantasie im Zelt verschwindet und alle Spieler ihr folgen. Nun setzt sich Abu Kital auf den Thron, wobei seine Gestalt den Zuschauern durch die Steinlehne verdeckt wird. Rechts und links von ihm und überall lassen sich die andern nieder, doch so, daß sie den Zuschauern die Schattenbilder nicht verdecken. Es wird still. Die Stimme des Vorbeters erschallt hinter der Szene. Er tritt auf und singt:
 Heijh alas salâh! Heijh alal felah! Auf zum Gebet!
        Auf zum Heil! Heijh alas salâh! Heijh alal felah!""",
         """Bitte nicht stören."""]

inputs = pd.DataFrame(inputs)
inputs.columns = ["Text"]

inputs["type"] = "pred"

inputs["Text"] = inputs["Text"].astype(str)

dataset_inf = Dataset.from_pandas(inputs)

tokenized_dataset_inf = dataset_inf.map(
    tokenize_function,
    batched=True,
    remove_columns=["Text", "type"],
)

inf_dataloader = DataLoader(tokenized_dataset_inf, shuffle=False, collate_fn=collate_fn, batch_size=batch_size)

res = []
for step, batch in enumerate(tqdm(inf_dataloader)):
    
    logits = model(**batch.to("cuda"))["logits"]
    result = logits.detach().cpu().numpy()
    
    
    for r in result:
    
        res.append(r)

# output interpretation
classes = {0:"Joy", 1:"Anger", 2:"Sadness", 3:"Love", 4:"Fear", 5:"Agitation"}

def binarize(x):
    if x > 0:
        return 1
    else:
        return 0
vfunc = np.vectorize(binarize)
vfunc(np.array(res))

#array([[1, 0, 0, 0, 0, 0],  -> Joy
#       [0, 1, 0, 0, 1, 1],  -> Anger+Fear+Agitation
#       [0, 0, 1, 0, 0, 0],  -> Sadness
#       [0, 0, 0, 1, 0, 0],  -> Love
#       [0, 0, 0, 0, 1, 0],  -> Fear
#       [0, 0, 0, 0, 0, 1],  -> Agitation
#       [0, 0, 0, 0, 0, 0]]) -> No Emotion

