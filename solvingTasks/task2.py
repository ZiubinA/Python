#Scenario: You have a list of raw price strings from a web scrape: prices = ["$10.50", "$5.00", "Free", "$20.00"].
#Goal: Write one line of code that creates a new list containing only the float numbers (ignore "Free" and remove the "$").
import pandas as pd

prices = ["$10.50", "$5.00", "Free", "$20.00"]

prices_cleaned = [float(c.replace("$", "")) if c != "Free" else 0.0 for c in prices]
print(prices_cleaned)

ids = [101, 102, 101, 103, 104, 102, 105]
helplist = []
duplicates = []
for num in ids:
    if num in helplist:
        duplicates.append(num)
    else:
        helplist.append(num)
print(duplicates)

visitors = [55, 10, 55, 20, 10, 55, 30]
visits = set()
count = 0
#for i in visitors:
#    if i not in visits:
#        count = count + 1
#    visits.add(i)

visits = set(visitors)

#print(visits, count)
print(len(visits))

all_employees = {101, 102, 103, 104, 105}
swiped_badge = {101, 102, 104}

all = set(swiped_badge)
appsent = set()
for i in all_employees:
    if i not in all:
        appsent.add(i)
print(appsent)

internet_users = {1, 2, 3, 4, 5}
tv_users = {4, 5, 6, 7, 8}

both = set(internet_users) & set(tv_users)
print(both)

raw_emails = [
    "Jonas@Telia.com",
    "maria@gmail.com",
    "jonas@telia.com",  
    "MARIA@gmail.com",  
    "Admin@Telia.com"
]

unique_emails = set()
for i in raw_emails:
    unique_emails.add(i.lower())
print(unique_emails)

downloaded = {101, 102, 103, 104, 105, 106}
logged_in = {102, 104, 105, 107} 

gost = set(downloaded) - set(logged_in)
print(gost)

mobile = {1, 2, 3, 4, 5, 6}
broadband = {2, 3, 7, 8}
tv = {2, 3, 4, 9}

gold = set(mobile) & set(tv) & set(broadband)
mobile_only = set(mobile) - set(tv) - set(broadband)

print(gold)
print(mobile_only)
