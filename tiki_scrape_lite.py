# Import package
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re


# Send a request
url = 'https://tiki.vn/nha-sach-tiki/c8322'
r = requests.get(url)

# Loading data to BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')
products = soup.find_all('div', {'class': 'product-item'})
# articles = soup.find_all('article', {'class':'item-news'})

data = []
for product in products:
    d = {'Title': '',
         'Author': '',
         'Final_price': '',
         'Original_price': '',
         'Reviews': '',
         'Discount': ''}
    try:
        # Get name of item
        d['Title'] = product.a['title']
        # Get author
        d['Author'] = product.a.find('p', {'class': "author"}).text
        # Get final price
        final_price_temp = product.find('span', {"class": "final-price"}).text
        d['Final_price'] = re.sub(r'\D', '', final_price_temp)
        # Get Original price
        temp = product.find('span', {"class": "price-regular"}).text
        d['Original_price'] = re.sub(r'\D', '', temp)
        # Get discount if exist
        if product.find('span', {"class": "sale-tag sale-tag-square"}).text:
            d['Discount'] = product.find(
                'span', {"class": "sale-tag sale-tag-square"}).text

        # Get number of review (if exist)
        if product.find('p', {'class': 'review'}).text:
            temp = product.find('p', {'class': 'review'}).text
            d['Reviews'] = re.sub(r'\D', '', temp)

        # d['price-regular'] = product.a.find('span', {'class':"price-regular"}).text
        # d['sale-tag sale-tag-square'] = product.a.find('span', {'class':"sale-tag sale-tag-square"}).text
        # d['price-sale'] = product.a.find('span', {'class':"price-sale"}).text

        data.append(d)
    except:
        pass

pd.DataFrame(data=data, columns=data[0].keys())
