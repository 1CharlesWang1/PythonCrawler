import requests
from bs4 import BeautifulSoup
import re
import json

response= requests.get('https://ncov.dxy.cn/ncovh5/view/pneumonia')
page=response.content.decode()

soup=BeautifulSoup(page,'lxml')
print(soup)
script=soup.find(id='getAreaStat')
provinces_text=script.text

json_str=re.findall(r'(\[.*\])',provinces_text)[0]


#格式转换
last_day=json.loads(json_str)
print(last_day)


