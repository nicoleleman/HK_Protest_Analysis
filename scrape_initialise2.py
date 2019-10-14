from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import csv

link = 'https://www.chinadailyhk.com/articles/163/39/218/1570991239568.html?newsId=109599'
source  = requests.get(link).text
soup = BeautifulSoup(source, 'lxml')
#print(soup.p.get_text())
#print(soup.prettify())
page = soup.find('p').getText()
#print(page)

for article in soup.find_all('div', class_='news-cut-box'):
    title = article.h5.text
    print(f'Title: {title}')

    date = article.find('span', class_='news-date').text
    print(f'Date: {date}')

    article_text = article.find('div', class_='news-cut')
    #print(article_text)
    article_paragraph = article_text.find_all('p')
    #print(article_paragraph)
    main_body = []
    for paragraph in article_paragraph:
        main_body.append(paragraph.text)
    print(main_body)


