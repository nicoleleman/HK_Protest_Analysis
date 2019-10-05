from bs4 import BeautifulSoup
import requests
import csv

link = 'https://www.scmp.com/news/hong-kong/politics/article/3014737/nearly-2-million-people-take-streets-forcing-public-apology'
source  = requests.get(link).text
soup = BeautifulSoup(source, 'lxml')
print(soup.prettify())

for article in soup.find_all('div', class_='article__wrapper wrapper'):
    title = article.h1.text
    print(f'Title: {title}')

    #description = article.find('li', class_='generic-article__summary--li content--li').text
    #print(description)
    description = article.find_all('li', class_='generic-article__summary--li content--li')
    #description_text = description.text
    print(description)

    main_body = article.find('div', class_='row__details details').text
    print(main_body)

    main_body2 = article.find_all('p', class_='details__body body')
    print(main_body2)



