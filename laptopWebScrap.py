import requests
from bs4 import BeautifulSoup
import pandas  as pd

response = requests.get('https://books.toscrape.com/')
soup = BeautifulSoup(response.content,'html.parser')
titles=[]
title=soup.find_all('h3')
for i in title:
    titles.append(i.a['title'])

prices=[]
price=soup.find_all('p',class_='price_color')
for j in price:
    prices.append(j.get_text())

stocks=[]
stock=soup.find_all('p',class_='instock availability')
for k in stock:
    stocks.append(k.get_text().strip())

df=pd.DataFrame()
df['Name'] = titles
df['Price'] = prices
df['Stock Availability'] = stocks
df.to_csv("Books Scrape.csv")