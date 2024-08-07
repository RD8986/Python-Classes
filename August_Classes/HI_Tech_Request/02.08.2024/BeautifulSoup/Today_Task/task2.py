from bs4 import BeautifulSoup
import requests
response=requests.get("https://www.academy.indixpert.com/student-dashboard/learn-program")
var=response.text
soup=BeautifulSoup(var, "html.parser")
# print(soup.a)
# print(soup.find_all("a"))
print(soup.prettify)