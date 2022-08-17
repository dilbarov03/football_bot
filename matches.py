#match-rows__root > div:nth-child(2)
import requests
from lxml import etree
from bs4 import BeautifulSoup

HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
            'Accept-Language': 'en-US, en;q=0.5'})


url = "https://www.livescore.com/en/football/live/"

response = requests.get(url, headers=HEADERS)

soup = BeautifulSoup(response.content, 'html.parser')

dom = etree.HTML(str(soup))

print(response.text)
