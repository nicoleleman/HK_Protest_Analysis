import pandas as pd
import numpy
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
from collections import Counter

def count_frequent_words():
    df = pd.read_csv('csv_files/scmp_article_content_all.csv')
    text_dataset = df['paragraphs']
    #print(type(text_dataset.head()))

    split_it = text_dataset.str.split()
    #print(split_it)

    #counter = Counter(split_it)
    Counter = Counter(x for xs in split_it for x in xs)
    most_occur = Counter.most_common(10)
    print(most_occur)

nltk.download()