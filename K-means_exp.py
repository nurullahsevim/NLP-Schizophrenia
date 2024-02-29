# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 14:47:58 2022

@author: Nurullah
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 12:47:40 2022

@author: Nurullah
"""

import sys,os
from nltk.tokenize import word_tokenize
import nltk
import string
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import TruncatedSVD
from sklearn.cluster import KMeans


def load_embeddings():
    embedding_dict = {}
    filepath = './vectors.txt'
    with open(filepath,encoding="utf8") as f:
        for line in f:
            word,*vector = line.split()
            vector = np.array(vector, dtype=np.float32)
            vector = vector/np.linalg.norm(vector)
            embedding_dict.update({word:vector})
    f.close()
    return embedding_dict



stopwords = open("../stopwords.txt","r",encoding="utf-8").readlines()

for i in range(len(stopwords)):
    stopwords[i] = stopwords[i].strip()

kontrol_dir = "control_nlp/"

kontrol_files = os.listdir(kontrol_dir) 

for i in range(len(kontrol_files)-1,-1,-1):
    if not (".txt" in kontrol_files[i]):
        del kontrol_files[i]
        
        
        
sizo_dir = "sizo_nlp/"

sizo_files = os.listdir(sizo_dir)

embeddings = load_embeddings()
        
        

all_group_words_kontrol = set()
group_words_kontrol = []
all_group_words_sizo = set()
group_words_sizo = []

mean_similarity = []
min_similarity = []
var_similarity = []

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
    
    
    for a in list(string.punctuation)+["’","‘","“","”","0","1","2","3","4","5","6","7","8","9"]:
        all_words = all_words.replace(a," ") 
    all_words = all_words.lower()
    words = word_tokenize(all_words,language="turkish")
    
    
    # sim = []
    # for word_num in range(len(words)-1):
    #     try:
    #         w1 = embeddings[words[word_num]]
    #     except:
    #         continue
    #     try:
    #         w2 = embeddings[words[word_num+1]]
    #     except:
    #         continue
    #     sim.append(w1.T@w2)
    
    # sim = np.array(sim)
    # mean_similarity.append(np.mean(sim))
    # min_similarity.append(np.min(sim))
    # var_similarity.append(np.var(sim))
    
    # for a in stopwords:
    #     try:
    #         words.remove(a)
    #     except:
    #         pass
    
    all_group_words_kontrol = all_group_words_kontrol.union(set(words))
    group_words_kontrol.append(words)
    
    
"""
--------------------------------------------------------------------------------------------------------
"""
    
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
    
    
    for a in list(string.punctuation)+["’","‘","“","”","0","1","2","3","4","5","6","7","8","9"]:
        all_words = all_words.replace(a," ") 
    all_words = all_words.lower()
    words = word_tokenize(all_words,language="turkish")
    
#     sim = []
#     for word_num in range(len(words)-1):
#         try:
#             w1 = embeddings[words[word_num]]
#         except:
#             continue
#         try:
#             w2 = embeddings[words[word_num+1]]
#         except:
#             continue
#         sim.append(w1.T@w2)
    
#     sim = np.array(sim)
#     mean_similarity.append(np.mean(sim))
#     min_similarity.append(np.min(sim))
#     var_similarity.append(np.var(sim))
    
#     for a in stopwords:
#         try:
#             words.remove(a)
#         except:
#             pass
    
    all_group_words_sizo = all_group_words_sizo.union(set(words))
    group_words_sizo.append(words)
    
all_group_words = all_group_words_sizo.union(all_group_words_kontrol)
group_words = group_words_kontrol + group_words_sizo



sizo_vecs = []
control_vecs = []

for ind in group_words_sizo:
    ind_vec = np.zeros((300,))
    for word in ind:
        try:
            ind_vec+=embeddings[word]
        except:
            pass
    sizo_vecs.append(ind_vec/len(ind))
sizo_vecs = np.array(sizo_vecs)

for ind in group_words_kontrol:
    ind_vec = np.zeros((300,))
    for word in ind:
        try:
            ind_vec+=embeddings[word]
        except:
            pass
    control_vecs.append(ind_vec)
control_vecs = np.array(control_vecs)
    
predictions = KMeans(n_clusters=2).fit_predict(np.append(control_vecs, sizo_vecs,axis=0))
from sklearn.manifold import TSNE
labels = np.append(np.zeros((38,)), np.ones((38,)))
accuracy = sum(labels==predictions)/76
X_embedded = TSNE(n_components=2,random_state=42).fit_transform(np.append(control_vecs, sizo_vecs,axis=0))
fig, ax = plt.subplots(1, 1, figsize=(8,3))
for x,l,p in zip(X_embedded, labels,predictions):
    if l:
        if p:
            ax.scatter(x[0], x[1], marker = '.', c = 'green')
        else:
                ax.scatter(x[0], x[1], marker = '.', c = 'red')
    else:
        if p:
            ax.scatter(x[0], x[1], marker = 'x', c = 'red')
        else:
                ax.scatter(x[0], x[1], marker = 'x', c = 'green')
ax.scatter(0,0, marker = '.', c = 'grey',label="Control")
ax.scatter(0,0, marker = 'x', c = 'grey',label="Patient")
ax.legend()



# group_stats = []
# word_count = dict.fromkeys(all_group_words, 0)
# N = len(all_group_words)
# # keys = 
# for subject in group_words:
#     stats = dict.fromkeys(all_group_words, 0)
#     for word in subject:
#         stats[word]+=1
#         word_count[word]+=1
#     group_stats.append(stats)
# group_stats_np = np.zeros((0,N))
# for stat in group_stats:
#     group_stats_np = np.append(group_stats_np, np.array(list(stat.values())).reshape(1,N),axis=0)
    

# group_stats_sizo = []
# word_count_sizo = dict.fromkeys(all_group_words_sizo, 0)
# N = len(all_group_words_sizo)
# # keys = 
# for subject in group_words_sizo:
#     stats = dict.fromkeys(all_group_words_sizo, 0)
#     for word in subject:
#         stats[word]+=1
#         word_count_sizo[word]+=1
#     group_stats_sizo.append(stats)
# group_stats_np_sizo = np.zeros((0,N))
# for stat in group_stats_sizo:
#     group_stats_np_sizo = np.append(group_stats_np_sizo, np.array(list(stat.values())).reshape(1,N),axis=0)
    
    
    
    
# group_stats_kontrol = []
# word_count_kontrol = dict.fromkeys(all_group_words_kontrol, 0)
# N = len(all_group_words_kontrol)
# # keys = 
# for subject in group_words_kontrol:
#     stats = dict.fromkeys(all_group_words_kontrol, 0)
#     for word in subject:
#         stats[word]+=1
#         word_count_kontrol[word]+=1
#     group_stats_kontrol.append(stats)
# group_stats_np_kontrol = np.zeros((0,N))
# for stat in group_stats_kontrol:
#     group_stats_np_kontrol = np.append(group_stats_np_kontrol, np.array(list(stat.values())).reshape(1,N),axis=0)    

    
    

# svd = TruncatedSVD(n_components=20, n_iter=7, random_state=42)
# lsa_result = svd.fit_transform(group_stats_np)

# predictions = KMeans(n_clusters=2,random_state=4681).fit_predict(lsa_result)

# """
# # ---------------------------------------------------------------------------------------------------------------------
# """

# from sklearn.manifold import TSNE
# labels = np.append(np.zeros((38,)), np.ones((38,)))
# X_embedded = TSNE(n_components=2).fit_transform(lsa_result)
# fig, ax = plt.subplots(1, 1, figsize=(8,3))
# for x,l in zip(X_embedded, labels):
#     if l:
#         ax.scatter(x[0], x[1], marker = '.', c = 'c')
#     else:
#         ax.scatter(x[0], x[1], marker = 'x', c = 'darkviolet')
# ax.scatter(0,0, marker = '.', c = 'c',label="Conrtol")
# ax.scatter(0,0, marker = 'x', c = 'darkviolet',label="Patient")
# ax.legend()

