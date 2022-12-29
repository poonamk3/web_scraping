# Step.1: Install all the requirements 
# pip install requests
# pip install bs4
# pip install html5lib
# pip install lxml


import requests
from bs4 import BeautifulSoup as soup
import pandas as pd

html = requests.get('https://in.hotels.com/Hotel-Search?adults=2&d1=2023-01-12&d2=2023-01-13&destination=Indore%2C%20Madhya%20Pradesh%2C%20India&endDate=2023-01-13&latLong=22.719568%2C75.857727&regionId=1564&selected=&semdtl=&sort=RECOMMENDED&startDate=2023-01-12&theme=&useRewards=false&userIntent=')
bsobj=soup(html.content,'lxml')

price = []

for name in bsobj.findAll('div',{'class':'uitk-text uitk-type-600 uitk-type-bold uitk-text-emphasis-theme'}):
  price.append(name.text.strip())
# print(price)


names =[]
for name in bsobj.findAll('div',{'class':'uitk-spacing uitk-spacing-padding-blockend-three uitk-layout-flex-item'}):
  names.append(name.find_all('h2')[0].get_text())
# print(names)

review=[]

for name in bsobj.findAll('span',{'class':'uitk-text uitk-type-300 uitk-type-bold uitk-text-default-theme'}):
  review.append(name.text.strip())
# print(review)


no_review=[]
for name in bsobj.findAll('span',{'class':'uitk-text uitk-type-200 uitk-text-default-theme'}):
  no_review.append(name.text.strip())
# print(no_review)


d1 = {'Hotel':names,'Ratings':review,'No_of_Reviews':no_review,'Price':price}
# df = pd.DataFrame.from_dict(d1)
df = pd.DataFrame.from_dict(d1, orient='index')
ds = df.transpose()
print(ds)
