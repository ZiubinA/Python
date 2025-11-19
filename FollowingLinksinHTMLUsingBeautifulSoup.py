import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup 
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE  

def urlMeth(url):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser') 
    tags = soup('a')
    return tags
url = input("Enter url - ")
countEnt = int(input("Enter count -"))
posEnt = int(input("Enter position -"))
count = 0
i = 0

tags = urlMeth(url)

while i < countEnt:
    count = 1
    for tag in tags: 
        if count == posEnt:
            print ('Contents:',tag.contents[0])
            
            tags = urlMeth(tag.get('href', None))
            print("Retrieving: ", tag.get('href', None))
            break
        else: count = count + 1  
    i = i + 1

    

