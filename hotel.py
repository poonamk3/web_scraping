import requests
from bs4 import BeautifulSoup as soup
import pandas as pd
url="https://www.tripadvisor.in/Hotels-g187147-Paris_Ile_de_France-Hotels.html"
html = requests.get(url)
bsobj=soup(html.content,'lxml')

ratings = []
for rating in bsobj.findAll('a',{'class':'ui_bubble_rating'}):
  ratings.append(rating['alt'])

print(ratings)

"""names =[]
for name in bsobj.findAll('button',{'class':'text-left w-full truncate font-bold'}):
	names.append(name.find('span').text.strip())
	# names.append(name.select('button.text span')[0]
print(names)
"""

# hotel = []
# for name in bsobj.findAll('div',{'class':'biGQs _P fiohW alXOW NwcxK GzNcM ytVPx UTQMg RnEEZ ngXxk'}):
# 	hotel.append(name.text.strip())
# print(hotel)