import requests
from bs4 import BeautifulSoup as bs

r = requests.get("http://books.toscrape.com")

sourceCode = r.text

soup = bs(sourceCode, 'html.parser')

for bookName in soup.find_all('h3'):
    print(bookName.text)
