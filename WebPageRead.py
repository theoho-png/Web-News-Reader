from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import pandas as pd
import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

class Reader():

    def __init__(self, url):
        self.url = url

    def loadUrl(self):
        values = {'s':'basics', 'submit':'search'}
        data = urllib.parse.urlencode(values)
        data = data.encode('utf-8')
        req = urllib.request.Request(self.url, data)
        resp = urllib.request.urlopen(req)
        #https://www.youtube.com/watch?v=GEshegZzt3M
        return str(resp.read())
    
    def pFinder(self):
        data = []
        stopWords = set(stopwords.words("english"))
        content = soup.find("div", class_="article section")
        for passage in content.find_all("p", class_=""):
            words = re.sub('\\n','testing', passage.text)
            words = re.sub('\[.*?''""...]', '',words)
            words = re.sub('[%s]'%re.escape(string.punctuation), '', words)
            words = re.sub(r'^\w*\d\w', ' ', words)
            words = word_tokenize(words)
            for w in words:
                if w not in stopWords:
                    data.append(w)
        return data
        
    def topicFinder(self):
        content = soup.find("div", class_="header subheader")
        return content.find('h1').get_text()

class Trainer():

    def __init(self):
        self.content = list()
    
    def trainOut(self, string):
        topic = list()
        topic.append(string)
        return topic
    
def webState(url):
    link = urllib.request.urlopen(url)
    if (link.status == 200):
        return True
    else:
        return False

if __name__ == "__main__":
    #nltk.download()
    t = Trainer()
    i = 0
    pages = ["https://www.abc.net.au/news/2020-03-12/us-stocks-bear-market-as-coronavirus-sparks-recession-fears/12048310?section=business", "https://www.abc.net.au/news/2020-03-12/coronavirus-pandemic-suspends-nba-cancels-e3-and-major-events/12049670?section=politics", "https://www.abc.net.au/news/2020-03-12/coronavirus-provides-australian-sport-with-sense-of-dread/12050454?section=analysis", "https://www.abc.net.au/news/2020-03-11/formula-one-team-members-quarantined-due-to-coronavirus-fears/12047494?section=sport", "https://www.abc.net.au/news/science/2020-03-12/fossil-of-hummingbird-like-dinosaur-found-in-myanmar-amber/12033634", "https://www.abc.net.au/news/2020-03-12/nsw-minister-gareth-ward-found-naked-disorientated-by-police/12050738", "https://www.abc.net.au/news/2020-03-12/emerald-teen-daley-catip-join-prestigious-dance-academy/12039558"]
    while(i == 0) :
        r = Reader(pages[i])
        soup = BeautifulSoup(r.loadUrl(), 'html.parser')
        t.trainOut(r.topicFinder())
        print (r.pFinder())
        i += 1 