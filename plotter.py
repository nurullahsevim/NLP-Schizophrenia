# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 14:40:52 2022

@author: Nurullah
"""

import numpy as np
import matplotlib.pyplot as plt


materials = ['Control', 'Kardeş', 'Şizofren']
x_pos = np.arange(len(materials))
CTEs = [3.875, 10.783, 8.348]
error = [4.842, 9.704, 8.913]

fig, ax = plt.subplots()
ax.bar(x_pos, CTEs, yerr=error, align='center', alpha=0.5, ecolor='black', capsize=10)
ax.set_ylabel('Average First Personal Pronoun Size')
ax.set_xticks(x_pos)
ax.set_xticklabels(materials)
ax.set_title('Average Number of First Personal Pronoun Use')
ax.yaxis.grid(True)

# Save the figure and show
plt.tight_layout()
plt.savefig('ben.png')
plt.show()





# labels = ['Control', 'Kardeş', 'Şizofren']
# men_means = [358.333, 505.217, 431.304]
# women_means = [310.417, 446.957, 387.826]

# x = np.arange(len(labels))  # the label locations
# width = 0.35  # the width of the bars

# fig, ax = plt.subplots()
# rects1 = ax.bar(x - width/2, men_means, width, label='w/ Stopwords')
# rects2 = ax.bar(x + width/2, women_means, width, label='w/o Stopwords')

# # Add some text for labels, title and custom x-axis tick labels, etc.
# ax.set_ylabel('Average Number of Words')
# ax.set_title('Average Number of Words Used w/ and w/o Stopwords')
# ax.set_xticks(x, labels)
# ax.legend()

# ax.bar_label(rects1, padding=3)
# ax.bar_label(rects2, padding=3)

# fig.tight_layout()

# plt.show()


# kontrol_avg_word_sizes = np.load("kontrol_avg_word_sizes.npy")
# kontrol_avg_type_sizes = np.load("kontrol_avg_type_sizes.npy")

# kardes_avg_word_sizes = np.load("kardes_avg_word_sizes.npy")
# kardes_avg_type_sizes = np.load("kardes_avg_type_sizes.npy")

# sizo_avg_word_sizes = np.load("sizo_avg_word_sizes.npy")
# sizo_avg_type_sizes = np.load("sizo_avg_type_sizes.npy")


# fig, ax = plt.subplots()
# kontrol = plt.plot(kontrol_avg_word_sizes, kontrol_avg_type_sizes,label='Kontrol')
# kardes = plt.plot(kardes_avg_word_sizes, kardes_avg_type_sizes,label='Kardeş')
# sizo = plt.plot(sizo_avg_word_sizes, sizo_avg_type_sizes,label='Şizofren')

# # Add some text for labels, title and custom x-axis tick labels, etc.
# ax.set_xlabel('Word Size')
# ax.set_ylabel('Type Size')
# ax.set_title('Words/Types Growth Graph')
# ax.legend()

# fig.tight_layout()

# plt.show()
















