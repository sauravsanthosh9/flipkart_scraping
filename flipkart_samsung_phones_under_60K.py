import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import pandas as pd


base_url = "https://www.flipkart.com/search?q=samsung%20mobiles%20under%2060K&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
ua = UserAgent()
pages = 115


header ={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
all_data = []
  

for page in range(1, pages + 1):
  url=base_url.format(page)
  response=requests.get(url,headers=header).text
  data=BeautifulSoup(response,"html.parser")
  items=data.find_all("div",class_="KzDlHZ")
  price=data.find_all("div",class_="Nx9bqj _4b5DiR")
  
  for mobile_name, mobile_price in zip(items, price):
    name = mobile_name.get_text(strip=True)
    price_current = mobile_price.get_text(strip=True)
    all_data.append([name, price_current])

print(all_data)

df = pd.DataFrame(filter_data)

df.to_csv("samsung.csv",index=False)