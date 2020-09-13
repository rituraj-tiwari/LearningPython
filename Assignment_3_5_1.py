import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error

#url = 'http://py4e-data.dr-chuck.net/comments_963352.xml'
while True:
    url = input('The URL:')
    if len(url) < 1 : break
    html = urllib.request.urlopen(url).read()
    
    tree = ET.fromstring(html)
    res = tree.findall('comments/comment')
    print('Count: ', len(res))

    total = 0
    for i in res:
        x = i.find('count').text
        total = total + int(x)
    print('Sum: ', total)