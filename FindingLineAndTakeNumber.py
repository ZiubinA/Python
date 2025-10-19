# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("Wrong file name")
    quit()
count = 0
numbers = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1
    numberPos = line.find("0")
    endInd = line.find("/n")
    num = line[numberPos : endInd]
    numbers = float(numbers) + float(num)
print("Average spam confidence:", numbers / count)