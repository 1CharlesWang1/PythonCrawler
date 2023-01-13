import requests
from bs4 import BeautifulSoup

response= requests.get('https://ncov.dxy.cn/ncovh5/view/pneumonia')
page=response.content.decode()
# print(page)

soup=BeautifulSoup(page,'lxml')
script=soup.find(id='getAreaStat')
provinces_text=script.text
print(provinces_text)
