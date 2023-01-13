import requests

response=requests.get("http://www.baidu.com")

print(response)

response.encoding='utf-8'
print(response.text)

print(response.content)
print(response.content.decode())