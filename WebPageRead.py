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
paragraphs = re.findall(r'<p>(.*?)</p>', str(respData))
for eachP in paragraphs:
    print (eachP)
#https://www.youtube.com/watch?v=GEshegZzt3M """


#else:
#print("Unable to optain web page")

#with open() as urlFile: