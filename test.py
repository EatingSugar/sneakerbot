print("l")
import requests
print("l")
from bs4 import BeautifulSoup as bs
URL = "https://www.adidas.co.uk/nmd_r1-v2-shoes/FV9022.html"
page = requests.get(URL)
page = bs(page.content, 'html.parser')
print("l")
print(page)
print("s")