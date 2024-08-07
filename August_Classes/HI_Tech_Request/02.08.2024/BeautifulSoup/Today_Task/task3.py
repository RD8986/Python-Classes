from bs4 import BeautifulSoup
import requests
response=requests.get("https://www.tcs.com/sitemap.xml")
var=response.text
soup=BeautifulSoup(var,features="xml")
print(soup.prettify())