import requests
from bs4 import BeautifulSoup as soup
import pandas as pd
url = "https://www.booking.com/searchresults.html?label=gen173nr-1FCAEoggI46AdIM1gEaGyIAQGYATG4ARnIAQzYAQHoAQH4AQKIAgGoAgO4ArbPtZ0GwAIB0gIkNmE1NmI5NzYtMGQzYi00MzM4LWFmMmUtOGI1MmRhZTY3MTc02AIF4AIB&lang=en-us&sid=4d799e09c3c3e367284481b7f406aba8&sb=1&sb_lp=1&src=index&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Findex.html%3Flabel%3Dgen173nr-1FCAEoggI46AdIM1gEaGyIAQGYATG4ARnIAQzYAQHoAQH4AQKIAgGoAgO4ArbPtZ0GwAIB0gIkNmE1NmI5NzYtMGQzYi00MzM4LWFmMmUtOGI1MmRhZTY3MTc02AIF4AIB%26sid%3D4d799e09c3c3e367284481b7f406aba8%26sb_price_type%3Dtotal%26%26&ss=Indore%2C+India&is_ski_area=&checkin_year=2023&checkin_month=1&checkin_monthday=10&checkout_year=2023&checkout_month=1&checkout_monthday=12&efdco=1&group_adults=2&group_children=0&no_rooms=1&b_h4u_keep_filters=&from_sf=1&dest_id=-2097803&dest_type=city&search_pageview_id=3814479b7ff0023a&search_selected=true"
html = requests.get(url)
print("www.booking.com")
bsobj=soup(html.content,'lxml')


sapn=[]
for name in bsobj.findAll('span'):
  sapn.append(name)


price = []
for name in bsobj.findAll('div',{'class':'hotel-card__price bui-spacer--small'}):
  price.append(name.text.strip())


names =[]
for name in bsobj.findAll('h3',{'class':"bui-card__title"}):
  names.append(name.text.strip())


review=[]
for name in bsobj.findAll('span',{'class':'review-score-badge'}):
  review.append(name.text.strip())


no_review=[]
for name in bsobj.findAll('span',{'class':'review-score-widget__subtext'}):
  no_review.append(name.text.strip())





d1 = {'Hotel':names[:35],'Ratings':review[:35],'No_of_Reviews':no_review[:35],'Price':price[:35]}
# df = pd.DataFrame.from_dict(d1)
df = pd.DataFrame.from_dict(d1, orient='index')
ds = df.transpose()
print(ds)







