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