from bs4 import BeautifulSoup
import requests
import csv

link = 'https://www.scmp.com/news/hong-kong/politics/article/3014737/nearly-2-million-people-take-streets-forcing-public-apology'
source  = requests.get(link).text
soup = BeautifulSoup(source, 'lxml')
#print(soup.prettify())

for article in soup.find_all('div', class_='article__wrapper wrapper'):
    title = article.h1.text
    print(f'Title: {title}')

    descriptions = article.find_all('li', class_='generic-article__summary--li content--li')
    #print(descriptions)
    title_headers = []
    for li in descriptions:
        title_headers.append(li.getText())
    print(title_headers)

    main_body_text = []
    main_body = article.find('div', class_='row__details details').text
    print(main_body)

    main_body2 = article.find_all('div', class_='details__body body')
    print(main_body2)
    for div in main_body2:
        main_body_text.append(div.getText())
    print(main_body_text)

    test = article.find_all(class_='generic-article__body article-details-type--p content--p')
    print(test)
    #for div in main_body2



