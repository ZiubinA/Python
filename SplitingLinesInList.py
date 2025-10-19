fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line.rstrip()
    line = line.split()
    for word in line:
        if word in lst : continue
        lst.append(word)
lst.sort()
print(lst)