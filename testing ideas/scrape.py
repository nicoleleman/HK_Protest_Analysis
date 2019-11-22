from bs4 import BeautifulSoup
from datetime import datetime
import requests

# with open('simple.html', 'r') as html_file:
#     soup = BeautifulSoup(html_file, 'lxml')
#
# match = soup.title.text
# #print(match)
# match2 = soup.div
# #print(match2)
# match3 = soup.find('div', class_='footer')
# #print(match3)
#
# # Get all article headline and summary
# for article in soup.find_all('div', class_='article'):
#     headline = article.h2.a.text
#     print(headline)
#     summary = article.p.text
#     print(summary)
#    print()

#ts = 1284101485
#print(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))

url = 'https://apigw.scmp.com/content-delivery/v1?operationName=gettopicbyentityuuid&variables={"latestContentsLimit":50,"latestOpinionsLimit":50,"entityUuid":"21363753-95b4-43cc-bf62-3fd61ff77877","articleTypeId":"012d7708-2959-4b2b-9031-23e3d025a08d","applicationIds":["2695b2c9-96ef-4fe4-96f8-ba20d0a020b3"],"after":"1571135522000"}&extensions={"persistedQuery":{"version":1,"sha256Hash":"e1586e5b5b2f1f63a3d84ec54864eab377d6291c88270911bbc2a76e26addab9"}}'

headers = {'apikey': 'MyYvyg8M9RTaevVlcIRhN5yRIqqVssNY'}
resp = requests.get(url, headers=headers)
data = resp.json()['data']
page_info = data['topic']['latestContentsWithCursor']['pageInfo']
items = data['topic']['latestContentsWithCursor']['items']
 # assigns the endcursor for each section to the variable after
after = str(1571135522000)
print(data)

'''
from bs4 import BeautifulSoup
import requests
import csv

link = 'https://www.scmp.com/topics/hong-kong-protests'
source = requests.get(link).text
soup = BeautifulSoup(source, 'html5lib')

csv_file = open('scmp_scrape.csv', 'w')

csv_writer = csv.writer((csv_file))
csv_writer.writerow(['Title','Summary', 'Time', 'Article Link'])

'''
Scrape through temporary main article
'''
main_temp_article = soup.find('div', \
    class_='article-level article-level-five article article-area\
    __main-content main-content flow--responsive style--default')

main_temp_article_title = soup.find('a', class_='article-title__article-link article-hover-link')
main_temp_article_title_text = main_temp_article_title.getText()
print(f'Main Temporary Article: {main_temp_article_title_text}')

try:
    main_temp_article_summary = soup.find('li', class_='article-level-five__summary--li content--li')
    main_temp_article_summary_text = main_temp_article_summary.getText()
    print(main_temp_article_summary_text)
except Exception as e:
    main_temp_article_summary_text = None

'''
Scrape through list of articles
'''
for article in soup.find_all('div', \
class_='article-level article-level-three article article-area__content content thumb--large'):

    article_heading = article.find('a', class_='article__link')
    article_heading_text = article_heading.getText()
    print(f'Article Title: {article_heading_text}')

    try:
        article_summary = article.find('p', class_='article-level-three__summary--p content--p')
        article_summary_text = article_summary.getText()
        print(article_summary_text)

    except Exception as e:
        article_summary_text = None

    time = article.find('span', class_='status-left__time')
    article_time = time.getText()
    print(article_time)

    raw_link = article_heading.get('href')
    final_link = 'https://scmp.com/print' + raw_link
    print(final_link)
    print()

    csv_writer.writerow([article_heading_text,article_summary_text, article_time, final_link])

csv_file.close()
'''