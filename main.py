import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://www.arise.tv'
category = 'category/global/page'

n = 317
for number in range(n):
    url = f'{BASE_URL}/{category}/{number+1}'
    print(f'Scraping page {number+1}...')
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    for data in soup.find_all('article'):
        titles = data.find('h3')   
        print(titles.text.strip())
 

