from bs4 import BeautifulSoup
import pandas as pd
import requests
import csv
path = 'scmp_articles_2020_01_10.csv'

# with open (path, 'r') as f:
#     reader = csv.reader(f)
#     list_of_url = []
#     for row in reader:
#         list_of_url.append(row[2])
#         print(row[2])


link = 'https://www.scmp.com/print/news/hong-kong/politics/article/3014737/nearly-2-million-people-take-streets-forcing-public-apology'
source = requests.get(link).text
soup = BeautifulSoup(source, 'html5lib')
print(soup.prettify())

with open('scmp_article_content.csv', 'w', newline='') as f:
    fieldnames = ['title', 'summary', 'date', 'main_text_title', 'paragraphs']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    article_text_list = []

    for article in soup.find_all('div', class_='article__wrapper wrapper'):
        title = article.h1.text
        print(f'Title: {title}')

        for summaries in article.find_all('li', class_='print-article__summary--li content--li'):
            summary = summaries.getText()
            print(f'Summary >>>> {summary}')

        date_published = article.find('p', class_='last-update__published published')
        date = date_published.time.getText()
        print(f'Date Published >>>> {date[10:]}')

        for main_text in article.find_all('div', class_='print-article__body article-details-type--p content--p'):
            main_text_title = main_text.getText()
            print(f'Main Text Title >>>> {main_text_title}')

        for main_text2 in article.find_all('p', class_='print-article__body article-details-type--p content--p'):
            paragraphs = main_text2.getText()
            article_text_list.append(paragraphs)
            article_text_conc = ' '.join(article_text_list)
            print(f'Article Text >>>> {paragraphs}')

        for item in article:
            # unix timestamp included the millisecond so divide by 1000 is required
            writer.writerow({'title': title, 'summary': summary,'date': date, \
                             'main_text_title': main_text_title, 'paragraphs': article_text_conc})
            #except Exception as e:
                #writer.writerow({'title': '', 'summary': '', 'date': '', 'main_text_title': '', 'paragraphs': ''})

print(article_text_conc)
