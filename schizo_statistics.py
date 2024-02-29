# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 22:15:03 2022

@author: Nurullah
"""

import sys,os
from nltk.tokenize import word_tokenize
import nltk
import string
import numpy as np
import matplotlib.pyplot as plt

sizo_dir = "sizo_nlp/"

sizo_files = os.listdir(sizo_dir)
stopwords = open("../stopwords.txt","r",encoding="utf-8").readlines()

for i in range(len(stopwords)):
    stopwords[i] = stopwords[i].strip()


word_sizes = []
type_sizes = []
word_sizes_ns = []
type_sizes_ns = []
tekil_sahıs = []
tekil_sahıs_freq = []
t_t_ratio = []
t_t_ratio_ns = []
sentence_length = []



for j in range(len(sizo_files)):
# for file in kontrol_files:
    text = open(sizo_dir+sizo_files[j],"r",encoding="utf-8").readlines()
    for i in range(len(text)-1,-1,-1):
        text[i] = (text[i].strip())
        if len(text[i])<2:
            del text[i]

    
    tald = text
    
    tald_words = ""
    for i in range(len(tald)):
        if (not "?" == tald[i][-1]):
            tald_words+=tald[i]+" "
        
    all_words = tald_words
    
    
    
    
    pncts = list(string.punctuation)+["’","‘","“","”","0","1","2","3","4","5","6","7","8","9"]
    pncts.remove("!")
    pncts.remove(".")
    pncts.remove("?")
    for a in pncts:
        all_words = all_words.replace(a," ") 
    all_words = all_words.lower()
    
    all_words = all_words.replace("!",".")
    all_words = all_words.replace("?",".")
    all_sentences = all_words.split(".")
    sen_ln = []
    for sentence in all_sentences:
        sntc_wrds = word_tokenize(sentence,language="turkish")
        sen_ln.append(len(sntc_wrds))
    sentence_length.append(sum(sen_ln)/float(len(sen_ln)))
    
    """
    
    words = word_tokenize(all_words,language="turkish")
    b_words = []
    
    for wrd in words:
        b_words.append("--"+wrd)
    
    count = 0
    for wrd in b_words:
        if "--ben" in wrd:
            count+=1
    
    tekil_sahıs.append(count)

    
    
    
    word_set=set()
    set_size = []
    word_size = []
    for i in range(0,len(words),10):
        try:
            word_set.update(words[i:i+10])
        except:
            word_set.update(words[i:])
        set_size.append(len(word_set))
        word_size.append(i+10)
    
    
    # word_sizes.append(word_size)
    # type_sizes.append(set_size)
    word_sizes.append(word_size[-1])
    type_sizes.append(set_size[-1])

    for a in stopwords:
        try:
            words.remove(a)
        except:
            pass
        
    word_set_ns=set()
    set_size_ns = []
    word_size_ns = []
    for i in range(0,len(words),10):
        try:
            word_set_ns.update(words[i:i+10])
        except:
            word_set_ns.update(words[i:])
        set_size_ns.append(len(word_set_ns))
        word_size_ns.append(i+10)
        
    # word_sizes_ns.append(word_size_ns)
    # type_sizes_ns.append(set_size_ns)
    word_sizes_ns.append(word_size_ns[-1])
    type_sizes_ns.append(set_size_ns[-1])
    tekil_sahıs_freq.append(count/word_size[-1])

    ratios = []
    for i in range(0,len(words)):
        try:
            wordss = words[i:i+50]
            word_set = set(wordss)
        except:
            wordss = words[i:]
            word_set = set(wordss)
        ratios.append(len(word_set)/len(wordss))
    ratios = np.array(ratios)
    t_t_ratio.append(np.mean(ratios))
    

    for a in stopwords:
        try:
            words.remove(a)
        except:
            pass
        
    ratios = []
    for i in range(0,len(words)):
        try:
            wordss = words[i:i+50]
            word_set = set(wordss)
        except:
            wordss = words[i:]
            word_set = set(wordss)
        ratios.append(len(word_set)/len(wordss))
    ratios = np.array(ratios)
    t_t_ratio_ns.append(np.mean(ratios))
    
    
tekil_sahıs_freq = np.array(tekil_sahıs_freq)
tekil_sahıs = np.array(tekil_sahıs)

f = open("sizo_grup_statistics.txt","w")
f.write("----------------------------------------\n")
f.write("Average first personal noun frequency: " + str(np.round(np.mean(tekil_sahıs_freq),3))+u"\u00B1"+str(np.round(np.std(tekil_sahıs_freq),3))+"\n")
# f.close()

t_t_ratio = np.array(t_t_ratio)
t_t_ratio_ns = np.array(t_t_ratio_ns)

# f = open("sizo_grup_statistics.txt","a")
f.write("\n----------------------------------------\n")
f.write("Average MATTR (w/ Stopwords): " + str(np.round(np.mean(t_t_ratio),3))+u"\u00B1"+str(np.round(np.std(t_t_ratio),3))+"\n")
f.write("Average MATTR (w/o Stopwords): " + str(np.round(np.mean(t_t_ratio_ns),3))+u"\u00B1"+str(np.round(np.std(t_t_ratio_ns),3))+"\n")
f.close()
    
# max_len = 0
# max_seq = None
# for szs in word_sizes:
#     if len(szs)>max_len:
#         max_len = len(szs)
#         max_seq = szs

# mod_word_sizes = []
# for i in range(len(word_sizes)):
#     mod_word_sizes.append(max_seq)

# for i in range(len(type_sizes)):
#     last = type_sizes[i][-1]
#     for j in range(len(type_sizes[i]),max_len):
#         type_sizes[i].append(last)
        
# avg_word_sizes = np.mean(np.array(mod_word_sizes),axis=0)
# avg_type_sizes = np.mean(np.array(type_sizes),axis=0)

# np.save("sizo_avg_word_sizes", avg_word_sizes)
# np.save("sizo_avg_type_sizes", avg_type_sizes)



# max_len = 0
# max_seq = None
# for szs in word_sizes_ns:
#     if len(szs)>max_len:
#         max_len = len(szs)
#         max_seq = szs

# mod_word_sizes = []
# for i in range(len(word_sizes_ns)):
#     mod_word_sizes.append(max_seq)

# for i in range(len(type_sizes_ns)):
#     last = type_sizes_ns[i][-1]
#     for j in range(len(type_sizes_ns[i]),max_len):
#         type_sizes_ns[i].append(last)
        
# avg_word_sizes = np.mean(np.array(mod_word_sizes),axis=0)
# avg_type_sizes = np.mean(np.array(type_sizes_ns),axis=0)

# np.save("sizo_avg_word_sizes_ns", avg_word_sizes)
# np.save("sizo_avg_type_sizes_ns", avg_type_sizes)



# word_sizes = np.array(word_sizes)
# type_sizes = np.array(type_sizes)
# word_sizes_ns = np.array(word_sizes_ns)
# type_sizes_ns = np.array(type_sizes_ns)

f = open("sizo_grup_statistics.txt","a")
f.write("Before stop-word removal:\n")
f.write("Average words used: "+str(np.round(np.mean(word_sizes),3))+u"\u00B1"+str(np.round(np.std(word_sizes),3))+"\n")
f.write("Average word types used: "+str(np.round(np.mean(type_sizes),3))+u"\u00B1"+str(np.round(np.std(type_sizes),3))+"\n")
f.write("After stop-word removal:\n")
f.write("Average words used: "+str(np.round(np.mean(word_sizes_ns),3))+u"\u00B1"+str(np.round(np.std(word_sizes_ns),3))+"\n")
f.write("Average word types used: "+str(np.round(np.mean(type_sizes_ns),3))+u"\u00B1"+str(np.round(np.std(type_sizes_ns),3)))
f.write("\n----------------------------------------\n")
f.write("Average first personal noun usage: " + str(np.round(np.mean(tekil_sahıs),3))+u"\u00B1"+str(np.round(np.std(tekil_sahıs),3))+"\n")
f.close()

"""