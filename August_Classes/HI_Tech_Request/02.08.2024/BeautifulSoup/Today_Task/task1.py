from bs4 import BeautifulSoup
import requests
response=requests.get("https://www.netflix.com/in/")
# print(response.text)
var=response.text
soup=BeautifulSoup(var,"html.parser")
# print(soup.name)
# print(soup.title)
# print(soup.find_all(search="netflix"))
