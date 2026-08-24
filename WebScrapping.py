""" request

--> request module is used to sent the HTTP request to the server

 Beautifulsoup module:
--> bs4 is version of the module,which is used to get the data from the website
h3--HTML tag
a--anchor tag

 Web Scrapping:
--> The process of collecting data from the websites with the normal python program is called as web scarping """

import requests
url_="https://books.toscrape.com/"
response=requests.get(url_)
print(response.status_code)

import requests
from bs4 import BeautifulSoup
url_="https://books.toscrape.com/"
response=requests.get(url_)
titl_=BeautifulSoup(response.text,'html.parser')
print(titl_.title) 

import requests
from bs4 import BeautifulSoup
url_="https://books.toscrape.com/"
response=requests.get(url_)
titl_=BeautifulSoup(response.text,'html.parser')
books=titl_.find_all('h3')
for book in books:
    titl_=book.find('a').get('title')
    print(titl_)
