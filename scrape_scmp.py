from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
import requests
import csv

'''
Function to scrape a list of articles and their data
'''
def scrape_all_links(url_link):
    # The variable after stores the endCursor of the previous page
    after = ''
    with open('scmp_articles_2020_02_23.csv', 'w', newline='') as f:
        fieldnames = ['socialHeadline', 'headline', 'urlAlias', 'updatedDate']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        # This for loop gets the site content using an api call
        for i in range(150):
            print('>>>>', i, after)
            headers = {'apikey': 'MyYvyg8M9RTaevVlcIRhN5yRIqqVssNY'}
            resp = requests.get(url_link, headers=headers)
            data = resp.json()['data']
            page_info = data['topic']['latestContentsWithCursor']['pageInfo']
            items = data['topic']['latestContentsWithCursor']['items']
            # assigns the endcursor for each section to the variable after
            after = str(page_info['endCursor'])

            try:
                for item in items:
                    if 'news' in item['urlAlias']:
                        # unix timestamp included the millisecond so divide by 1000 is required
                        converted_date = datetime.utcfromtimestamp(item['updatedDate'] / 1000).strftime(
                            '%Y-%m-%d %H:%M:%S')
                        social_headline = '"' + item['socialHeadline'] + '"'
                        headline = '"' + item['headline'] + '"'
                        new_url = 'https://scmp.com/print' + str(item['urlAlias'])
                        writer.writerow({'socialHeadline': social_headline, 'headline': headline,
                                         'urlAlias': new_url, 'updatedDate': converted_date})
            except Exception as e:
                writer.writerow({'socialHeadline': '', 'headline': '', 'urlAlias': '', 'updatedDate': ''})
    return;

url = 'https://apigw.scmp.com/content-delivery/v1?operationName=gettopicbyentityuuid&variables=\
{"latestContentsLimit":30,"latestOpinionsLimit":30,"entityUuid":"21363753-95b4-43cc-bf62-3fd61ff77877", \
"articleTypeId":"012d7708-2959-4b2b-9031-23e3d025a08d","applicationIds":["2695b2c9-96ef-4fe4-96f8-ba20d0a020b3"], \
"after":"' + after + '"}&extensions={"persistedQuery":{"version":1, \
"sha256Hash":"b0c6f88d4512241449827157f74e02abd2e311be6f4e33d4837ac6f723a03cb1"}}'
scrape_all_links(url)


''' 
Function to scrape each individual article
'''
def scrape_articles(path):
    file_path = 'csv_files/scmp_articles_2020_02_23.csv'
    list_of_url = []
    # Open the CSV file scmp_articles and import all article URLs into a list
    with open (path, 'r') as url_file:
        reader = csv.reader(url_file)
        next(reader, None)
        for row in reader:
            list_of_url.append(row[2])
    #print(list_of_url[0:10])

    with open('scmp_article_content_part4.csv', 'w', newline='', encoding='utf-8-sig') as f:
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