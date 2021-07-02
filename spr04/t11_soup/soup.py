from bs4 import BeautifulSoup
import requests
import sys
import json
url = sys.argv[1]

try:
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, 'html.parser')
    links = soup.findAll('a', class_="reference external")
    res = []
    for l in links:
        ltitle = requests.get(l.get('href'))
        lsoup = BeautifulSoup(ltitle.content, 'html.parser')
        title = soup.find('title')
        res.append({"link_text": l.contents[0], "url": l.get('href'), "title": title.string})
    jsonString = json.dumps(res)
    heading = soup.find("h1").string
    print(heading)
    jsonFile = open(heading, "w")
    jsonFile.write(jsonString)
    jsonFile.close()
except Exception as e:
    s = e