import requests
import pandas as pd
from bs4 import BeautifulSoup
                                    
response=requests.get('https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off')

soup=BeautifulSoup(response.content,'html.parser')

names=soup.find_all('div',class_='KzDlHZ')
name=[]
for i in names:
    d=i.getText()
    name.append(d)

prices=soup.find_all('div',class_='Nx9bqj _4b5DiR')
price=[]
for j in prices:
    d=j.getText()
    price.append(d)

rates=soup.find_all('div',class_="XQDdHH")
ratings=[]
for k in rates:
    d=k.getText()
    ratings.append(d)
    
image=soup.find_all('img',class_="DByuf4")
images=[]
for l in image:
    d=l['src']
    images.append(d)

link=soup.find_all('a',class_="CGtC98")
links=[]
for m in link:
    d='https://www.flipkart.com'+m['href']
    links.append(d)

length=min(len(name),len(price),len(ratings),len(images),len(links))

name = name[:length]
price = price[:length]
ratings = ratings[:length]
images = images[:length]
links = links[:length]

df=pd.DataFrame()
df['Name']=name
df['Price']=price
df['Ratings']=ratings
df['Images']=images
df['link']=links
df.to_csv('Mobiles Data.csv')