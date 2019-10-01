from bs4 import BeautifulSoup
import requests

source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source, 'lxml')

article = soup.find('article')
#print(article.prettify())

headline = article.h2.a.text
print(headline)

summary = article.find('div', class_='entry-content').p.text
print(summary)

video_source = article.find('iframe', class_='youtube-player')['src']
#print(video_source)

#Grabs the video id
video_id = video_source.split('/')[4]
video_id = video_id.split('?')[0]
#print(video_id)

yt_link = f'https://youtube.com/watch?v={video_id}'
print(yt_link)
