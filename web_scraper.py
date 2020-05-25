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
first_p = soup.p.a
#print(first_p)

description_tag = first_article.find('p', {'class':'description'})
#print(description_tag.prettify)


# 1. Data is the CONTENT of the tag

# Extract the content of the tag
description = description_tag.text
# print(description)

# 2. Data is the VALUE of an ATTRIBUTE of the tag

# Select the <a> tag inside description_tag
a_tag = description_tag.a
print(a_tag['title'])

# Putting it all together
data = []
articles = soup.find_all('article', {'class':'item-news'})

for article in articles:
        d = {'title':'', 'description': '', 'url': '', 'image_url': ''}
    try:
        d['title'] = article.a['title']
        d['description'] = article.p.text
        d['url'] = article.a['href']
        d['image_url'] = article.img['scr']
        data.append(d)

    except:
        pass

# Package into Functions

def get_url(url):
    """Get parsed HTML from url
    Input: url to the webpage
    Output: Parsed HTML text of the webpage
    """
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parse')

    return soup


def scrape_vnexpress(url='https://vnexpress.net/'):
    """Scrape the home page of vnexpress
    Input: url to the homepage. Default: https://vnexpress.net/
    Output: A list containing scraped data of all articles
    """
    soup = get_url(url)

    articles = soup.find_all('articles', {'class':'item-news'})


    for article in articles:
        d = {'title': '',
            'description': '',
            'url': '',
            'image_url': ''
            }
        try:
            d['title'] = article.a['title']
            d['description'] = article.p.text
            d['url'] = article.a['href']
            d['image_url'] = article.img['scr']
            data.append(d)

        except:
            pass

    return data



















