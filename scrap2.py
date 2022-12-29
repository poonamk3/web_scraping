# If you want to scrape a website:
# 1. Use the API
# 2. HTML web scraping using some tool like bs
# Step.1: Install all the requirements 
# pip install requests
# pip install bs4
# pip install html5lib

import requests
from bs4 import BeautifulSoup
url = "https://www.codewithharry.com"

# Step.2: Get the Html

r = requests.get(url)
htmlContent = r.content

# print(htmlContent)

# Step.2: Parse the Html

soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup)
# print(soup.prettify)

# Step.3: Html Tree traversal
# Commonly used types of objects:
# 1. Tag = print(type(title))
# 2. NavigableString = print(type(title.string))
# 3. BeautifulSoup = print(type(soup))
# 4. Comment

markup ='<p><!-- this is comment --></p>'
soup2 = BeautifulSoup(markup)
# print(type(soup2.p))
# exit()

title = soup.title  # get the title of the Html page
# print(type(title))
# print(type(soup))
# print(type(title.string))
# print(title)

paras = soup.find_all('p') # get the paragraph of the Html page
# print(paras)

# Get first element in the Html page
# print(soup.find('p'))

# get classes of any element in the Html page
# print(soup.find('p')['class'])

# find all the elements with class lead
# print(soup.find_all('p', class_="lead"))

# Get the text from the tags/soup
# print(soup.find('p').get_text())

# print(soup.get_text())
"""
# get all the anchor tags from the page
anchors = soup.find_all('a')
all_links = set()
# print(anchors)

# Get all the links on the page:
for link in anchors:
    if (link.get('href') != "#"):
        linkText = "https://codewithharry.com" +link.get('href')
        all_links.add(link)
        # print(linkText)



navbarSupportedContent = soup.find(id='navbarSupportedContent')
# .contents - A tag's children are available as a list 
# .children - A tag's children are available as a generator
# for elem in navbarSupportedContent:
    # print(elem)
    
# for item in codewithharry.stripped_strings:
    # print(item)
    
# for item in codewithharry.strings:
    # print(item)
    
# print(navbarSupportedContent.parent)
#  for item in navbarSupportedContent.parents: 
#     print(item)

# print(navbarSupportedContent.next_sibling.next_sibling)
# print(navbarSupportedContent.previous_sibling.previous_sibling)

elem = soup.select('.loginModal')
print(elem)
elem = soup.select('.modal-footer')
print(elem)

"""