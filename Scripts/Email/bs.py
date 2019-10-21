#!/ ~/.virtualenv/WebScrap/bin/python3

from urllib.request import urlopen 
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None

    try:
        bsObj = BeautifulSoup(html.read())
        title = bsObj.html.body.h2
    except AttributeError as e:
        return None

    return title

title = getTitle("https://mail.google.com/mail/u/0/#inbox/FMfcgxvzLrJVsSbmWhvWccqgHfLJncxM")
if title is None:
    print("Title not found")
else:
    print(title)