import pandas as pd
import numpy
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from collections import Counter


def count_frequent_words():
    global Counter
    df = pd.read_csv('csv_files/scmp_article_content_all.csv')
    text_dataset = df['paragraphs']
    #print(type(text_dataset.head()))

    split_it = text_dataset.str.split()
    #print(split_it)

    #counter = Counter(split_it)
    Counter = Counter(x for xs in split_it for x in xs)
    most_occur = Counter.most_common(10)
    print(most_occur)
    return most_occur

count_frequent_words()

# plt.figure(figsize=(16,6))
# pd_most_occur = pd.DataFrame(most_occur, columns = ['Words' , 'Count'])
# ax = sns.barplot(x='Count', y='Words' , data=pd_most_occur, palette='rocket')
# ax.set_ylabel('Count', fontsize=15)
# ax.set_xlabel('Words', fontsize=15)
# ax.set_title('Top 10 most common words', fontsize=20)

