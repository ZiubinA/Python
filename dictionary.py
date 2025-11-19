name = input("Enter file:")

if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

diction = {}

for line in handle:
    line = line.rstrip()
    if not line.startswith("From ") : continue
    line = line.split()
    word = line[1]
    diction[word] = diction.get(word, 0) + 1

maxCount = 0

for b in list(diction.values()):
    if b > maxCount: maxCount = b

for a,b in list(diction.items()):
    if b == maxCount: print(a,b) 
        