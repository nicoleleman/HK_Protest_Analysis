from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
import requests
import csv

file_path = '../../data/raw/hkfp_article_links_2020_06_21.csv'
list_of_url = []

# Open the CSV file and import all article URLs into a list
with open(file_path, 'r', encoding='utf-8') as url_file:
    reader = csv.reader(url_file)
    next(reader, None)
    for row in reader:
        list_of_url.append(row[3])
#print(list_of_url[0:10])

with open('../../data/processed/hkfp_article_content.csv', 'w', newline='', encoding='utf-8-sig') as f:
    fieldnames = ['title', 'date', 'main_text_title', 'tags', 'url']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    i = 1599

    test = list_of_url[1599:]
    for url in test:
        source = requests.get(url).text
        soup = BeautifulSoup(source, 'html.parser')
        article_tags = []
        article_main_text = []

        try:
            header_content = soup.find('header', class_='entry-header')
            title = header_content.h1.text
            date = header_content.time.text

            main_content = soup.find('div', class_='entry-content')
            for p in main_content.find_all('p')[:-1]:
                paragraphs = p.text
                article_main_text.append(paragraphs)
                article_main_text_conc = '; '.join(article_main_text)

            footer_content = soup.find('span', class_='tags-links')
            for t in footer_content.find_all('a'):
                    tags = t.text
                    article_tags.append(tags)
                    article_tags_conc = '; '.join(article_tags)

            writer.writerow({'title': title, 'date': date, 'main_text_title': article_main_text_conc, \
                                     'tags': article_tags_conc, 'url': url})
        except Exception as e:
            title = 'NaN'
            date = 'NaN'
            paragraphs = 'NaN'
            article_main_text.append(paragraphs)
            article_main_text_conc = '; '.join(article_main_text)
            tags = 'NaN'
            article_tags.append(tags)
            article_tags_conc = '; '.join(article_tags)
            writer.writerow({'title': title, 'date': date, 'main_text_title': article_main_text_conc, \
                             'tags': article_tags_conc, 'url': url})

        print('Number >>>> {}'.format(i))
        print(url)
        i += 1