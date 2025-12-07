import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter location: ')
if len(url) < 1: 
    url = "http://py4e-data.dr-chuck.net/comments_42.json"

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()

print('Retrieved', len(data), 'characters')

try:
    info = json.loads(data)
except:
    info = None

if not info:
    print('==== Failure To Retrieve ====')
    exit()

comments = info.get('comments', []) 

print('User count:', len(comments))

total_sum = 0
for item in comments:
    print('Name', item['name'])
    print('Count', item['count'])
    total_sum = total_sum + int(item['count'])

print('Sum:', total_sum)