fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("data file do not exists")

for line in fh:
    line = line.rstrip()
    print(line.upper())