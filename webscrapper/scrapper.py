from bs4 import BeautifulSoup
import urllib.request

listt = ["hello","bye","good+day"]

def search(searchStr):
    req = urllib.request.Request(
    url="https://www.google.com/search?q="+searchStr,
    headers={'User-Agent': ' Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0'})
    handler = urllib.request.urlopen(req)
    with handler as response:
        soup = BeautifulSoup(response, 'html.parser')
        for resultStats in soup.find_all("div", {"id": "resultStats"}):
            print(resultStats)
            
for searchString in listt:
    search(searchString)
