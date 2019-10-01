from bs4 import BeautifulSoup
import requests

source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source, 'lxml')

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
