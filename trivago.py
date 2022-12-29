
import requests
from bs4 import BeautifulSoup as soup
import pandas as pd
url="https://www.tripadvisor.in/Hotels-g187147-Paris_Ile_de_France-Hotels.html"
html = requests.get(url)
bsobj=soup(html.content,'lxml')
print(bsobj)