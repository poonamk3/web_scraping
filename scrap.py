import requests
from bs4 import BeautifulSoup
url = "https://www.google.com"


r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup)

markup ='<p><!-- this is comment --></p>'
# print(markup)
soup2 = BeautifulSoup(markup)
# print(soup2)



# title =soup.title
# # print(title)
# # print(type(title))
# # print(type(title.string))


# b = soup.body
# # print(b)

# meta = soup.meta
# # print(type(meta))


# paras = soup.find_all('p')
# # print(paras)

# anchor = soup.find_all('a')
# # print(anchor)


# header = soup.find_all('script')
# # print(header)
