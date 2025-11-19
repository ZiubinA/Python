name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
diction = dict()
for line in handle:
    line = line.rstrip()
    if not line.startswith("From "): continue
    line = line.split()
    for word in line:
        if ':' in word:
            parts = word.split(':')
            hours = parts[0]
            diction[hours] = diction.get(hours, 0) + 1
            continue

newList = list()
for a,b in diction.items():
    newtup = (a, b)
    newList.append(newtup)

newList = sorted(newList)

for val, key in newList:
    print(val, key)