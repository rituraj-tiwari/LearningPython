import urllib, urllib.request
from bs4 import BeautifulSoup

#url = 'http://py4e-data.dr-chuck.net/known_by_Lynsie.html'
url = input('The URL:')
count = int(input('Enter the count:'))
position = int(input('Enter the position:'))-1
html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html,"html.parser")
href = soup('a')
print(href)

for i in range(count):
    link = href[position].get('href', None)
    print (href[position].contents[0])
    html = urllib.request.urlopen(link).read()
    soup = BeautifulSoup(html,"html.parser")
    href = soup('a')