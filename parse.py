from bs4 import BeautifulSoup
import time
import os
cwd = os.path.dirname(__file__)
htmlFilePath = os.path.join(cwd, 'resp.html')
with open(file=htmlFilePath, mode='r', encoding='utf8') as htmlFile:
    soup = BeautifulSoup(htmlFile, 'lxml')
    leafs = soup.select('div div.hp-list ul li')
    for leaf in leafs:
        a = leaf.a
        span = leaf.span
        absHref = a.attrs['href']
        if a.text.startswith('学术报告：') and 'list-time' in span.attrs['class'] :
            timeStr = span.text
            month, day = timeStr.split('/')
            # publishTime = time.strptime(timeStr, "%m/%d") 
    
    print()

# soup = BeautifulSoup()