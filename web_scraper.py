import requests
from bs4 import BeautifulSoup

# get the data
r = requests.get('https://vnexpress.net/')

# load data into bs4
soup = BeautifulSoup(r.text, 'html.parser')

# First occurence of the tag
first_article = soup.find('article', {'class':'item-news'})
# print(first_article.prettify())
# All occurences of the tags
articles = soup.find_all('article', {'class': 'item-news'})
# print(articles)
# First occurence of the tag w/o attribue
first_p = soup.p
# print(first_p)






















