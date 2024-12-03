import argparse
import os
import re

## MAKE custom changes here ####
# os.environ["CUDA_VISIBLE_DEVICES"]="0"
# os.environ['TRANSFORMERS_CACHE'] = '/mnt2/data/sentiment-datasets/leo/cache/'
# os.environ['TOKENIZERS_PARALLELISM'] = "false"

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
import spacy as sp

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
#model.cuda()
model.eval()

tokenizer.pad_token_id = tokenizer.eos_token_id
model.config.pad_token_id = tokenizer.pad_token_id

def tokenize_function(examples):
    # max_length=None => use the model max length (it's actually the default)
    outputs = tokenizer(examples["Text"], truncation=True, max_length=max_len)
    return outputs

def collate_fn(examples):
    return tokenizer.pad(examples, padding="longest", return_tensors="pt")

def chunks(xs, n):
    n = max(1, n)
    return [xs[i:i+n] for i in range(0, len(xs), n)]




### replace inputs with whatever you want to put throught the model ###
inputs = ["This is a test","This is a test."]

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

model.cuda()
res = []
for step, batch in enumerate(tqdm(inf_dataloader)):
    
    logits = model(**batch)["logits"]
    result = logits.detach().numpy()
    
    
    for r in result:
    
        res.append(r)
        
    if step % 1000 == 0:
        pd.DataFrame(res).to_csv("output.tsv", sep="\t")

pd.DataFrame(res).to_csv("output.tsv", sep="\t")  


