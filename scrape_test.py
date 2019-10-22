from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('cms_scrape.csv', 'w')

csv_writer = csv.writer((csv_file))
csv_writer.writerow(['Headline','Summary','Video Link'])

for article in soup.find_all('article'):
    headline = article.h2.a.text
    print(f'This is the headline: {headline}')

    summary = article.find('div', class_='entry-content').p.text
    print(f'This is the summary: {summary}')

    try:
        video_source = article.find('iframe', class_='youtube-player')['src']

        video_id = video_source.split('/')[4]
        video_id = video_id.split('?')[0]

        yt_link = f'https://youtube.com/watch?v={video_id}'
    except Exception as e:
        yt_link = None

    print(yt_link)
    print()

    csv_writer.writerow([headline,summary,yt_link])

csv_file.close()