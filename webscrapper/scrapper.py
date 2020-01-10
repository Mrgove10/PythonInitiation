from bs4 import BeautifulSoup
import urllib.request
import sys

scoretab = []


def score(listresult):
    total = 0
    listresult.sort(reverse=True)
    for t in listresult:
        total += t
    percent = listresult[0] / total
    print(percent*100)


def search(searchStr):
    req = urllib.request.Request(
        url="https://www.google.com/search?hl=en&q="+searchStr,
        headers={'User-Agent': ' Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0'})
    handler = urllib.request.urlopen(req)
    with handler as response:
        soup = BeautifulSoup(response, 'html.parser')
        for resultStats in soup.find_all("div", {"id": "resultStats"}):
            string = resultStats.contents[0]  # gets the content
            stringsplit = string.split()  # splits the string
            stringtoint = int(stringsplit[1].replace(',', ''))  # transformes the string to an int
            scoretab.append(stringtoint) 
            print(searchStr, " ", stringtoint)

try : 
    for i in range(1, len(sys.argv)):
        search(sys.argv[i])
    score(scoretab)
    exit(0)
except IndexError:
    print("pas asset d'aguments")
    exit(1)