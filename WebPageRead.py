from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import re

#url = "https://www.abc.net.au/news/2020-03-11/coronavirus-stimulus-package-to-include-billions-for-apprentices/12046688"

class Reader:

    def loadUrl(self):
        values = {'s':'basics', 'submit':'search'}
        data = urllib.parse.urlencode(values)
        data = data.encode('utf-8')
        req = urllib.request.Request(url, data)
        resp = urllib.request.urlopen(req)
        #https://www.youtube.com/watch?v=GEshegZzt3M
        return str(resp.read())

    def finder(self):
        data = ""
        content = soup.find("div", class_="article section")
        for passage in content.find_all("p", class_=""):
            data += passage.text
            data = re.sub(r'[^\w]', ' ', data)
        return data

if __name__ == "__main__":
    print("Pleas input news link.")
    url = input()
    r = Reader()
    soup = BeautifulSoup(r.loadUrl(), 'html.parser')
    
    print(r.finder())
