import requests
from bs4 import BeautifulSoup

url = "https://www.dica.gov.mm/en/myindy/private-enterprises"

# get the url
r = requests.get(url)

htmlContent = (r.content)
# print(htmlContent)

# parse html
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify)

# HTML tree traversal
# title = soup.title
# print(type(title))
# paras = soup.find_all("a")['class']
# print(paras)
# print(soup.find_all('div', class_='view-content'))

# get the text from the element
# print(soup.get_text())

# get all the link in the page

anchors = soup.find_all('a')

all_link = set()

for link in anchors:
    if(link.get('href') !='#'):
        linkText = ("https://www.dica.gov.mm/"+link.get('href'))
        all_link.add(link)
        print(linkText)

# contect_find = soup.find(id='view-content')

for data in soup.findAll('div',{'class':'view-content'}):
    print(data)