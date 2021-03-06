from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
import requests
import csv

''' 
Function to scrape each individual article
'''
def scrape_articles(file_name):
    file_path = '../../data/raw/{}'.format(file_name)
    list_of_url = []
    # Open the CSV file scmp_articles and import all article URLs into a list
    with open (file_path, 'r') as url_file:
        reader = csv.reader(url_file)
        next(reader, None)
        for row in reader:
            list_of_url.append(row[2])
    #print(list_of_url[0:10])

    with open('../../data/processed/name_of_csv_containing_article_data', 'w', newline='', encoding='utf-8-sig') as f:
        fieldnames = ['title', 'summary', 'date', 'main_text_title', 'paragraphs','url']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        # Loop over the list of URLs
        for url in list_of_url[2001:3001]:
            source = requests.get(url).text
            soup = BeautifulSoup(source, 'html5lib')
            article_text_list = []
            article_main_text = []
            article_summary = []

            for article in soup.find_all('div', class_='article__wrapper wrapper'):
                title = article.h1.text
                print(f'Title: {title}')

                date_published = article.find('p', class_='last-update__published published')
                date = date_published.time.getText()
                print(f'Date Published >>>> {date[10:]}')

                for summaries in article.find_all('li', class_='print-article__summary--li content--li'):
                    article_summary.append(summaries.getText())
                    article_summary_conc = '; '.join(article_summary)
                    print(f'Summary >>>> {article_summary_conc}')

                for main_text in article.find_all('div', class_='print-article__body article-details-type--p content--p'):
                    article_main_text.append(main_text.getText())
                    article_main_text_conc = '; '.join(article_main_text)
                    print(f'Main Text Title >>>> {article_main_text_conc}')

                for main_text2 in article.find_all('p', class_='print-article__body article-details-type--p content--p'):
                    paragraphs = main_text2.getText()
                    article_text_list.append(paragraphs)
                    article_text_conc = ' '.join(article_text_list)
                    print(f'Article Text >>>> {article_text_conc}')

                try:
                # unix timestamp included the millisecond so divide by 1000 is required
                    writer.writerow({'title': title, 'summary': article_summary_conc,'date': date[11:], \
                                 'main_text_title': article_main_text_conc, 'paragraphs': article_text_conc, 'url': url})
                except Exception as e:
                    writer.writerow({'title': '', 'summary': '', 'date': '', 'main_text_title': '', 'paragraphs': '', 'url': ''})
    return;

scrape_articles(file_path)