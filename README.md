# Unity-of-Literary-Change
[Coprus download](https://owncloud.gwdg.de/index.php/s/zcSKoprkSdARgdK)
# Paper
Leonard Konle, Merten Kröncke, Fotis Jannidis, Simone Winko (2024): On the Unity of Literary Change. 
The Development of Emotions in German Poetry, Prose, and Drama between 1850 and 1920 as a Test Case.
In Proceedings of the Computational Humanities Research Conference 2024 (CHR). Arrhus, Denmark.

# Detailed Test Results

Detailed table with test results for all combinations of variables and LAGs from the paper:

| Variable | Test | GenreX | GerneY | stat | pval | crit@5% | LAG |
| :------ | :------: | :------: | :------: | :------: | :------: | :------: | ------:|
| Emotionality | Not tested | Play | Prose | nan | nan | nan | nan | nan | 
| Emotionality | Not tested | Play | Poetry | nan | nan | nan | nan | nan | 
| Emotionality | Not tested | Prose | Play | nan | nan | nan | nan | nan | 
| Emotionality | Engle-Granger | Prose | Poetry | -2.47898931374954 | 0.288006658822286 | -3.99730479289940 | nan | nan | 
| Emotionality | Not tested | Poetry | Play | nan | nan | nan | nan | nan | 
| Emotionality | Engle-Granger | Poetry | Prose | -3.07849103662751 | 0.093339934522254 | -3.99730479289940 | nan | nan | 
| positive | Pearson Corr. | Play | Prose | -0.23054132253155 | 0.278450062444205 | nan | 0.0 | nan | 
| positive | Granger Causality | Play | Prose | 2.810574637147216 | 0.109207386944544 | nan | 1.0 | nan | 
| positive | Granger Causality | Play | Prose | 1.371076458255282 | 0.280519130458027 | nan | 2.0 | nan | 
| positive | Granger Causality | Play | Prose | 1.677738374887776 | 0.217245723226431 | nan | 3.0 | nan | 
| positive | Not tested | Play | Poetry | nan | nan | nan | nan | nan | 
| positive | Pearson Corr. | Prose | Play | -0.23054132253155 | 0.278450062444205 | nan | 0.0 | nan | 
| positive | Granger Causality | Prose | Play | 8.202721818993538 | 0.009592818391662 | nan | 1.0 | Yes | 
| positive | Granger Causality | Prose | Play | 2.199494444285056 | 0.141407739306582 | nan | 2.0 | nan | 
| positive | Granger Causality | Prose | Play | 0.961523155140348 | 0.438137243275941 | nan | 3.0 | nan | 
| positive | Not tested | Prose | Poetry | nan | nan | nan | nan | nan | 
| positive | Not tested | Poetry | Play | nan | nan | nan | nan | nan | 
| positive | Not tested | Poetry | Prose | nan | nan | nan | nan | nan | 
| negative | Pearson Corr. | Play | Prose | -0.16404062136573 | 0.443711027316900 | nan | 0.0 | nan | 
| negative | Granger Causality | Play | Prose | 3.608094853739042 | 0.072017641784849 | nan | 1.0 | nan | 
| negative | Granger Causality | Play | Prose | 2.154965835268760 | 0.146510363474348 | nan | 2.0 | nan | 
| negative | Granger Causality | Play | Prose | 2.8822967781925 | 0.073264528354734 | nan | 3.0 | nan | 
| negative | Not tested | Play | Poetry | nan | nan | nan | nan | nan | 
| negative | Pearson Corr. | Prose | Play | -0.16404062136573 | 0.443711027316900 | nan | 0.0 | nan | 
| negative | Granger Causality | Prose | Play | 8.236946014810899 | 0.009466233179908 | nan | 1.0 | Yes | 
| negative | Granger Causality | Prose | Play | 2.8883763625898 | 0.083202327015876 | nan | 2.0 | nan | 
| negative | Granger Causality | Prose | Play | 1.362974569750148 | 0.294636632008890 | nan | 3.0 | nan | 
| negative | Not tested | Prose | Poetry | nan | nan | nan | nan | nan | 
| negative | Not tested | Poetry | Play | nan | nan | nan | nan | nan | 
| negative | Not tested | Poetry | Prose | nan | nan | nan | nan | nan | 
| Joy | Pearson Corr. | Plays | Prose | -0.22543148432026 | 0.28953695975186 | nan | 0.0 | nan | 
| Joy | Granger Causality | Plays | Prose | 2.653281720383464 | 0.118986907417041 | nan | 1.0 | nan | 
| Joy | Granger Causality | Plays | Prose | 2.035947177951804 | 0.161188999375654 | nan | 2.0 | nan | 
| Joy | Granger Causality | Plays | Prose | 2.273914034967146 | 0.124783892425917 | nan | 3.0 | nan | 
| Joy | Not tested | Plays | Poetry | nan | nan | nan | nan | nan | 
| Joy | Pearson Corr. | Prose | Plays | -0.22543148432026 | 0.28953695975186 | nan | 0.0 | nan | 
| Joy | Granger Causality | Prose | Plays | 9.888681003137584 | 0.005100800468137 | nan | 1.0 | Yes | 
| Joy | Granger Causality | Prose | Plays | 3.864653580718172 | 0.041353689795512 | nan | 2.0 | Yes | 
| Joy | Granger Causality | Prose | Plays | 2.521428381510546 | 0.100070030175512 | nan | 3.0 | nan | 
| Joy | Not tested | Prose | Poetry | nan | nan | nan | nan | nan | 
| Joy | Not tested | Poetry | Plays | nan | nan | nan | nan | nan | 
| Joy | Not tested | Poetry | Prose | nan | nan | nan | nan | nan | 
| Anger | Pearson Corr. | Plays | Prose | 0.032323152392215 | 0.880815221805439 | nan | 0.0 | nan | 
| Anger | Granger Causality | Plays | Prose | 0.548056124639026 | 0.467715586118926 | nan | 1.0 | nan | 
| Anger | Granger Causality | Plays | Prose | 0.258783056485983 | 0.774977024303426 | nan | 2.0 | nan | 
| Anger | Granger Causality | Plays | Prose | 2.630535198912601 | 0.090954440428121 | nan | 3.0 | nan | 
| Anger | Not tested | Plays | Poetry | nan | nan | nan | nan | nan | 
| Anger | Pearson Corr. | Prose | Plays | 0.032323152392215 | 0.880815221805439 | nan | 0.0 | nan | 
| Anger | Granger Causality | Prose | Plays | 0.060616336317359 | 0.808033616298315 | nan | 1.0 | nan | 
| Anger | Granger Causality | Prose | Plays | 0.251718024867578 | 0.780310908527443 | nan | 2.0 | nan | 
| Anger | Granger Causality | Prose | Plays | 0.369507801986646 | 0.776207687320110 | nan | 3.0 | nan | 
| Anger | Not tested | Prose | Poetry | nan | nan | nan | nan | nan | 
| Anger | Not tested | Poetry | Plays | nan | nan | nan | nan | nan | 
| Anger | Not tested | Poetry | Prose | nan | nan | nan | nan | nan | 
| Sadness | Pearson Corr. | Plays | Prose | -0.30123944570243 | 0.152584389497492 | nan | 0.0 | nan | 
| Sadness | Granger Causality | Plays | Prose | 6.172641715652867 | 0.021948219537700 | nan | 1.0 | Yes | 
| Sadness | Granger Causality | Plays | Prose | 2.675547880022576 | 0.097673301614467 | nan | 2.0 | nan | 
| Sadness | Granger Causality | Plays | Prose | 1.561549219817066 | 0.242899234366063 | nan | 3.0 | nan | 
| Sadness | Pearson Corr. | Plays | Poetry | -0.28008164603823 | 0.184978557122909 | nan | 0.0 | nan | 
| Sadness | Granger Causality | Plays | Poetry | 0.030880596101456 | 0.862274090728569 | nan | 1.0 | nan | 
| Sadness | Granger Causality | Plays | Poetry | 0.074571412450029 | 0.92844308149484 | nan | 2.0 | nan | 
| Sadness | Granger Causality | Plays | Poetry | 0.165437905872374 | 0.917882588523466 | nan | 3.0 | nan | 
| Sadness | Pearson Corr. | Prose | Plays | -0.30123944570243 | 0.152584389497492 | nan | 0.0 | nan | 
| Sadness | Granger Causality | Prose | Plays | 24.11469383120653 | 8.442179086911394 | nan | 1.0 | Yes | 
| Sadness | Granger Causality | Prose | Plays | 8.125360296575627 | 0.003338157383959 | nan | 2.0 | Yes | 
| Sadness | Granger Causality | Prose | Plays | 4.643943836998013 | 0.018688315100034 | nan | 3.0 | Yes | 
| Sadness | Pearson Corr. | Prose | Poetry | -0.10050330342747 | 0.640309863349568 | nan | 0.0 | nan | 
| Sadness | Granger Causality | Prose | Poetry | 2.225632228251402 | 0.151343143627095 | nan | 1.0 | nan | 
| Sadness | Granger Causality | Prose | Poetry | 1.619938019984193 | 0.227012160009239 | nan | 2.0 | nan | 
| Sadness | Granger Causality | Prose | Poetry | 1.333197789013590 | 0.303361648941388 | nan | 3.0 | nan | 
| Sadness | Pearson Corr. | Poetry | Plays | -0.28008164603823 | 0.184978557122909 | nan | 0.0 | nan | 
| Sadness | Granger Causality | Poetry | Plays | 0.047527859394768 | 0.829631178540510 | nan | 1.0 | nan | 
| Sadness | Granger Causality | Poetry | Plays | 0.147737559906365 | 0.863753077909148 | nan | 2.0 | nan | 
| Sadness | Granger Causality | Poetry | Plays | 0.240369267683840 | 0.866732300456974 | nan | 3.0 | nan | 
| Sadness | Pearson Corr. | Poetry | Prose | -0.10050330342747 | 0.640309863349568 | nan | 0.0 | nan | 
| Sadness | Granger Causality | Poetry | Prose | 0.504737797697883 | 0.485628436346627 | nan | 1.0 | nan | 
| Sadness | Granger Causality | Poetry | Prose | 0.219599605641791 | 0.805082251519296 | nan | 2.0 | nan | 
| Sadness | Granger Causality | Poetry | Prose | 0.085971189571899 | 0.966575406560767 | nan | 3.0 | nan | 
| Love | Pearson Corr. | Plays | Prose | -0.16394153392531 | 0.443990180239482 | nan | 0.0 | nan | 
| Love | Granger Causality | Plays | Prose | 2.101640629191065 | 0.162642193482474 | nan | 1.0 | nan | 
| Love | Granger Causality | Plays | Prose | 0.338295521266800 | 0.717676059812112 | nan | 2.0 | nan | 
| Love | Granger Causality | Plays | Prose | 1.301757737042236 | 0.312872511646810 | nan | 3.0 | nan | 
| Love | Not tested | Plays | Poetry | nan | nan | nan | nan | nan | 
| Love | Pearson Corr. | Prose | Plays | -0.16394153392531 | 0.443990180239482 | nan | 0.0 | nan | 
| Love | Granger Causality | Prose | Plays | 2.711758644426540 | 0.115234719733658 | nan | 1.0 | nan | 
| Love | Granger Causality | Prose | Plays | 0.146325495546749 | 0.864952846341313 | nan | 2.0 | nan | 
| Love | Granger Causality | Prose | Plays | 0.094862994832702 | 0.961620726902371 | nan | 3.0 | nan | 
| Love | Not tested | Prose | Poetry | nan | nan | nan | nan | nan | 
| Love | Not tested | Poetry | Plays | nan | nan | nan | nan | nan | 
| Love | Not tested | Poetry | Prose | nan | nan | nan | nan | nan | 
| Fear | Not tested | Plays | Prose | nan | nan | nan | nan | nan | 
| Fear | Not tested | Plays | Poetry | nan | nan | nan | nan | nan | 
| Fear | Not tested | Prose | Plays | nan | nan | nan | nan | nan | 
| Fear | Pearson Corr. | Prose | Poetry | 0.021340127576969 | 0.921158297517843 | nan | 0.0 | nan | 
| Fear | Granger Causality | Prose | Poetry | 0.420363399471379 | 0.524130629976971 | nan | 1.0 | nan | 
| Fear | Granger Causality | Prose | Poetry | 0.030588122826471 | 0.969928213175639 | nan | 2.0 | nan | 
| Fear | Granger Causality | Prose | Poetry | 1.930170470669724 | 0.171127227076468 | nan | 3.0 | nan | 
| Fear | Not tested | Poetry | Plays | nan | nan | nan | nan | nan | 
| Fear | Pearson Corr. | Poetry | Prose | 0.021340127576969 | 0.921158297517843 | nan | 0.0 | nan | 
| Fear | Granger Causality | Poetry | Prose | 3.14815766880821 | 0.091238125335802 | nan | 1.0 | nan | 
| Fear | Granger Causality | Poetry | Prose | 3.053769400417794 | 0.073605362961832 | nan | 2.0 | nan | 
| Fear | Granger Causality | Poetry | Prose | 2.515023269176406 | 0.100636095622791 | nan | 3.0 | nan | 
| Agitation | Not tested | Plays | Prose | nan | nan | nan | nan | nan | 
| Agitation | Pearson Corr. | Plays | Poetry | -0.11338552374191 | 0.597827996090503 | nan | 0.0 | nan | 
| Agitation | Granger Causality | Plays | Poetry | 1.278731569395283 | 0.271513554171223 | nan | 1.0 | nan | 
| Agitation | Granger Causality | Plays | Poetry | 0.583354780323931 | 0.568810377750819 | nan | 2.0 | nan | 
| Agitation | Granger Causality | Plays | Poetry | 0.804265345581634 | 0.512095092359516 | nan | 3.0 | nan | 
| Agitation | Not tested | Prose | Plays | nan | nan | nan | nan | nan | 
| Agitation | Not tested | Prose | Poetry | nan | nan | nan | nan | nan | 
| Agitation | Pearson Corr. | Poetry | Plays | -0.11338552374191 | 0.597827996090503 | nan | 0.0 | nan | 
| Agitation | Granger Causality | Poetry | Plays | 0.307563852190347 | 0.585328085919428 | nan | 1.0 | nan | 
| Agitation | Granger Causality | Poetry | Plays | 0.256652160938868 | 0.776581481584589 | nan | 2.0 | nan | 
| Agitation | Granger Causality | Poetry | Plays | 0.571476843613225 | 0.642985086775025 | nan | 3.0 | nan | 
| Agitation | Not tested | Poetry | Prose | nan | nan | nan | nan | nan | 
| Affection | Not tested | Play | Prose | nan | nan | nan | nan | nan | 
| Affection | Pearson Corr. | Play | Poetry | -0.17833607501786 | 0.404427814818013 | nan | 0.0 | nan | 
| Affection | Granger Causality | Play | Poetry | 1.636617120167043 | 0.215433799030685 | nan | 1.0 | nan | 
| Affection | Granger Causality | Play | Poetry | 1.001219373443754 | 0.388093555202370 | nan | 2.0 | nan | 
| Affection | Granger Causality | Play | Poetry | 1.919728236023530 | 0.172805792468184 | nan | 3.0 | nan | 
| Affection | Not tested | Prose | Play | nan | nan | nan | nan | nan | 
| Affection | Not tested | Prose | Poetry | nan | nan | nan | nan | nan | 
| Affection | Pearson Corr. | Poetry | Play | -0.17833607501786 | 0.404427814818013 | nan | 0.0 | nan | 
| Affection | Granger Causality | Poetry | Play | 3.429802760299734 | 0.078849983592456 | nan | 1.0 | nan | 
| Affection | Granger Causality | Poetry | Play | 1.438968949160963 | 0.264642463869840 | nan | 2.0 | nan | 
| Affection | Granger Causality | Poetry | Play | 0.839770469353154 | 0.494409273313510 | nan | 3.0 | nan | 
| Affection | Not tested | Poetry | Prose | nan | nan | nan | nan | nan | 
| Longing | Not tested | Play | Prose | nan | nan | nan | nan | nan | 
| Longing | Pearson Corr. | Play | Poetry | 0.172517501309370 | 0.420177689908599 | nan | 0.0 | nan | 
| Longing | Granger Causality | Play | Poetry | 0.208276113250041 | 0.653039191631495 | nan | 1.0 | nan | 
| Longing | Granger Causality | Play | Poetry | 2.860109139943608 | 0.084978602821788 | nan | 2.0 | nan | 
| Longing | Granger Causality | Play | Poetry | 1.936322784696132 | 0.170146671886156 | nan | 3.0 | nan | 
| Longing | Not tested | Prose | Play | nan | nan | nan | nan | nan | 
| Longing | Not tested | Prose | Poetry | nan | nan | nan | nan | nan | 
| Longing | Pearson Corr. | Poetry | Play | 0.172517501309370 | 0.420177689908599 | nan | 0.0 | nan | 
| Longing | Granger Causality | Poetry | Play | 0.241410376751166 | 0.628537904228210 | nan | 1.0 | nan | 
| Longing | Granger Causality | Poetry | Play | 0.518399685382149 | 0.604589079528268 | nan | 2.0 | nan | 
| Longing | Granger Causality | Poetry | Play | 0.627674466522341 | 0.609005378850289 | nan | 3.0 | nan | 
| Longing | Not tested | Poetry | Prose | nan | nan | nan | nan | nan | 
| Lust | Engle-Granger | Play | Prose | -5.61145770369784 | 1.001457609370024 | -3.69460001890359 | nan | Yes | 
| Lust | Not tested | Play | Poetry | nan | nan | nan | nan | nan | 
| Lust | Engle-Granger | Prose | Play | -2.71930148233287 | 0.192881221767071 | -3.69460001890359 | nan | nan | 
| Lust | Not tested | Prose | Poetry | nan | nan | nan | nan | nan | 
| Lust | Not tested | Poetry | Play | nan | nan | nan | nan | nan | 
| Lust | Not tested | Poetry | Prose | nan | nan | nan | nan | nan | 
| Sub_Love | Engle-Granger | Play | Prose | -6.23994513872923 | 4.177532247348129 | -3.69460001890359 | nan | Yes | 
| Sub_Love | Engle-Granger | Play | Poetry | -5.53468447925568 | 1.446041556132005 | -3.69460001890359 | nan | Yes | 
| Sub_Love | Engle-Granger | Prose | Play | -2.00943313557027 | 0.521631997951875 | -3.71183413223140 | nan | nan | 
| Sub_Love | Engle-Granger | Prose | Poetry | -10.6609345334842 | 5.730441145710867 | -3.69460001890359 | nan | Yes | 
| Sub_Love | Engle-Granger | Poetry | Play | -2.63876673741648 | 0.222280594874884 | -3.69460001890359 | nan | nan | 
| Sub_Love | Engle-Granger | Poetry | Prose | -3.66298221596705 | 0.020729728718579 | -3.69460001890359 | nan | nan | 
