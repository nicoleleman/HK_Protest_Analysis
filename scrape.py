from bs4 import BeautifulSoup
import requests

with open('simple.html', 'r') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

match = soup.title.text
#print(match)
match2 = soup.div
#print(match2)
match3 = soup.find('div', class_='footer')
#print(match3)

# Get all article headline and summary
for article in soup.find_all('div', class_='article'):
    headline = article.h2.a.text
    print(headline)
    summary = article.p.text
    print(summary)
    print()