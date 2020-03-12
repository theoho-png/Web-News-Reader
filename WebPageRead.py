from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import re

#url = input()
url = "https://www.abc.net.au/news/2020-03-11/coronavirus-stimulus-package-to-include-billions-for-apprentices/12046688"
values = {'s':'basics', 'submit':'search'}
data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
respData = resp.read()
#https://www.youtube.com/watch?v=GEshegZzt3M
htmlDoc = str(respData)

soup = BeautifulSoup(htmlDoc, 'html.parser')
soup = soup.find("div", class_="article section")

container = ""
filterList = [',', '.', '$', '\\', '/'', ''"']

for passage in soup.find_all("p", class_=""):
    container += passage.text
    container = re.sub(r'[^\w]', ' ', container)

print (container)