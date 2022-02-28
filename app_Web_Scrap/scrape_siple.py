from bs4 import BeautifulSoup
import json
import requests

with open('app_Web_Scrap/simple.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

for article in soup.find_all('div', class_='article'):

    headline = article.h2.a.text
    print(headline)

    summary = article.p.text
    print(summary)
    print()

    dict = [{" Header ": headline, " content ": " summary "}]
with open('scrapped_info.json', 'w') as dann:
    json.dump(dict, dann)
