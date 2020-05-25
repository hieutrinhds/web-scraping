import pandas as pd
import requests
from bs4 import BeautifulSoup
import pandas as pd


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


# Package into Functions



def scrape_vnexpress(url='https://vnexpress.net/'):
    """Scrape the home page of vnexpress
    Input: url to the homepage. Default: https://vnexpress.net/
    Output: A list containing scraped data of all articles
    """
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    articles = soup.find_all('article', {'class':'item-news'})

    data =[]
    for article in articles:
        d = {'title': '', 'url': '', 'image_url': '', 'description': ''}
        try:
            d['title'] = article.a['title']
            d['url'] = article.a['href']
            d['description'] = article.p.text.replace('\xa0', '').strip('\n')
            
            if article.img:
                d['image_url'] = article.img['src']
            data.append(d)

        except:
            pass
    
    return data


data = scrape_vnexpress()
df = pd.DataFrame(data=data, columns=data[0].keys())
print(df)
















