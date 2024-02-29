# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 14:35:04 2022

@author: Nurullah
"""


#%% imports
from transformers import pipeline, AutoModelForTokenClassification, AutoTokenizer
import sentencepiece
import pandas as pd
import sys,os
import numpy as np
import matplotlib.pyplot as plt




#%% loading pretrained model
model_checkpoint = "wietsedv/xlm-roberta-base-ft-udpos28-tr"
aggregation = "simple"


def setModel(model_checkpoint, aggregation):
    model = AutoModelForTokenClassification.from_pretrained(model_checkpoint)
    tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
    return pipeline('token-classification', model=model, tokenizer=tokenizer, aggregation_strategy=aggregation)

ner_pipeline = setModel(model_checkpoint, aggregation)




#%% getting data
input_text = "Mustafa Kemal Atatürk 1881 yılında Selanik'te doğdu."

kontrol_dir = "control_nlp/"

kontrol_files = os.listdir(kontrol_dir) 

for i in range(len(kontrol_files)-1,-1,-1):
    if not (".txt" in kontrol_files[i]):
        del kontrol_files[i]
        
        
        
sizo_dir = "sizo_nlp/"

sizo_files = os.listdir(sizo_dir)
all_outputs = []

#%% runnin the model on control



for j in range(len(kontrol_files)):
    # for file in kontrol_files:
    text = open(kontrol_dir+kontrol_files[j],"r",encoding="utf-8").readlines()
    for i in range(len(text)-1,-1,-1):
        text[i] = text[i].strip()
        if len(text[i])<2:
            del text[i]
    
    
    tald = text
    
    tald_words = ""
    for i in range(len(tald)):
        if (not "?" == tald[i][-1]):
            tald_words+=tald[i]+" "
        
        
    all_words = tald_words

    output = ner_pipeline(all_words)

    df = pd.DataFrame.from_dict(output)

    if aggregation != "none":
        df.rename(index=str,columns={'entity_group':'POS Tag'},inplace=True)
    else:
        df.rename(index=str,columns={'entity_group':'POS Tag'},inplace=True)
    
    cols_to_keep = ['word','POS Tag','score','start','end']
    df_final = df[cols_to_keep]
    all_outputs.append(output)
    

#%% runnin the model on patients


for j in range(len(sizo_files)):
    # for file in kontrol_files:
    text = open(sizo_dir+sizo_files[j],"r",encoding="utf-8").readlines()
    for i in range(len(text)-1,-1,-1):
        text[i] = text[i].strip()
        if len(text[i])<2:
            del text[i]
    
    
    tald = text
    
    tald_words = ""
    for i in range(len(tald)):
        if (not "?" == tald[i][-1]):
            tald_words+=tald[i]+" "
        
        
    all_words = tald_words
    
    output = ner_pipeline(all_words)

    df = pd.DataFrame.from_dict(output)

    if aggregation != "none":
        df.rename(index=str,columns={'entity_group':'POS Tag'},inplace=True)
    else:
        df.rename(index=str,columns={'entity_group':'POS Tag'},inplace=True)
    
    cols_to_keep = ['word','POS Tag','score','start','end']
    df_final = df[cols_to_keep]
    all_outputs.append(output)
    

#%% process information

cols = ["ADJ","ADP","ADV","AUX","CCONJ","DET","INTJ","NOUN","NUM","PART","PRON","PROPN","PUNCT","SCONJ","SYM","VERB","X"]
all_stats = []
treshold = 0

for outp in all_outputs:
    stat = dict.fromkeys(cols, 0)
    for word in outp:
        if word["score"]>treshold:
            stat[word["entity_group"]]+=1
    all_stats.append(stat)
df_all = pd.DataFrame.from_dict(all_stats)