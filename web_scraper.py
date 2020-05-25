import requests
from bs4 import BeautifulSoup

# get the data
data = requests.get(url)

# load data into bs4
soup = BeautifulSoup(data.text, 'html.parser')


























