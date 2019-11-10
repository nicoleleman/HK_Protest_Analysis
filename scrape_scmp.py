from bs4 import BeautifulSoup
import requests
import csv

link = 'https://www.scmp.com/print/news/hong-kong/politics/article/3014737/nearly-2-million-people-take-streets-forcing-public-apology'
source = requests.get(link).text
soup = BeautifulSoup(source, 'html5lib')
#print(soup.prettify())


for article in soup.find_all('div', class_='article__wrapper wrapper'):
    title = article.h1.text
    print(f'Title: {title}')

    for summaries in article.find_all('li', class_='print-article__summary--li content--li'):
        print(f'Summary: {summaries.getText()}')

    date_published = article.find('p', class_='last-update__published published')
    date = date_published.time.text
    print(date)

    for main_text in article.find_all('div', class_='print-article__body article-details-type--p content--p'):
        print(main_text)

    for main_text2 in article.find_all('p', class_='print-article__body article-details-type--p content--p'):
        paragraphs = main_text2.text
        print(paragraphs)




