import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup as bs 


# sample youtube video url

video_url = "https://www.youtube.com/watch?v=MQ3O_hXb8MY"

# init an HTML Session

session = HTMLSession()

# get the html content

response = session.get(video_url)

# execute java-script

response.html.render(sleep=1)

# create bs object to parse HTML

soup = bs(response.html.html, "html.parser")

meta = soup.find_all("meta")

# print(meta)

title = soup.find_all("title")

# print(title)

image = soup.find_all("image")

# print(image)

discription = soup.find("discription")

# print(discription)

content = soup.find("meta", itemprop="name")["content"]

print(content)