import csv
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta, date


def daterange (start_date, end_date):
    for n in range(int( (end_date - start_date).days)):
        yield start_date + timedelta(n)

with open ('../../data/raw/hkfp_article_links_2020_06_21.csv', 'w', newline='', encoding='utf-8-sig') as f:
    fieldnames = ['title', 'datetime', 'date', 'url']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    start_date = date(2019, 7, 18)
    end_date = date(2020, 6, 22)

    for single_date in daterange(start_date, end_date):
        print(single_date.strftime("%Y/%m/%d"))
        url = "https://hongkongfp.com/{}".format(single_date.strftime("%Y/%m/%d"))
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        for articles in soup.find_all('main', class_='site-main'):
            try:
                published_date = articles.find('span', class_='posted-on').getText()
                published_datetime = articles.find('time', class_='entry-date published')['datetime']
            except Exception as e:
                published_date = 'NaN'
                published_datetime = 'NaN'

            for title_item in articles.find_all('h2', class_='entry-title'):
                title = title_item.getText()
                article_url = title_item.a['href']

                try:
                    # unix timestamp included the millisecond so divide by 1000 is required
                    writer.writerow({'title': title, 'datetime': published_datetime, 'date': published_date, \
                                     'url': article_url})
                except Exception as e:
                    writer.writerow(
                        {'title': '', 'datetime': '', 'date': '', 'url': ''})