from bs4 import BeautifulSoup
import pandas as pd
import requests
import csv

df = pd.read_csv('scmp_articles.csv', 'r', usecols=[3], error_bad_lines=False)
print(df.head())

#link = 'https://www.scmp.com/print/news/hong-kong/politics/article/3014737/nearly-2-million-people-take-streets-forcing-public-apology'
#source = requests.get(link).text
#soup = BeautifulSoup(source, 'html5lib')
#print(soup.prettify())

# with open('scmp_article_content.csv', 'w', newline='') as f:
#     fieldnames = ['title', 'summary', 'date', 'main_text_title', 'paragraphs']
#     writer = csv.DictWriter(f, fieldnames=fieldnames)
#     writer.writeheader()
#
#     for article in soup.find_all('div', class_='article__wrapper wrapper'):
#         title = article.h1.text
#         print(f'Title: {title}')
#
#         for summaries in article.find_all('li', class_='print-article__summary--li content--li'):
#             summary = summaries.getText()
#             print(f'Summary >>>> {summary}')
#
#         date_published = article.find('p', class_='last-update__published published')
#         date = date_published.time.getText()
#         print(f'Date Published >>>> {date[10:]}')
#
#         for main_text in article.find_all('div', class_='print-article__body article-details-type--p content--p'):
#             main_text_title = main_text.getText()
#             print(f'Main Text Title >>>> {main_text_title}')
#
#         for main_text2 in article.find_all('p', class_='print-article__body article-details-type--p content--p'):
#             paragraphs = main_text2.getText()
#             print(f'Article Text >>>> {paragraphs}')
#
#         for item in article:
#             # unix timestamp included the millisecond so divide by 1000 is required
#             writer.writerow({'title': title, 'summary': summary,'date': date, 'main_text_title': main_text_title, 'paragraphs': paragraphs})
#         # except Exception as e:
#         #     writer.writerow({'title': '', 'summary': '', 'date': '', 'main_text_title': '', 'paragraphs': ''})




