def isPalindrom(s):
    n = len(s)
    i = 0
    while i <= n / 2:
        if s[i] == s[n - i - 1]:
            i += 1
            continue
        else: return False
    return True

s = input()
print(isPalindrom(s))

def calValofString(s):
    count = 0
    for i in s:
        count += ord(i) - ord('a') + 1
    return count

print("write the word to count its weight")
s = input()
print(calValofString(s))

wordList = ["level", "robot", "radar", "data"]
palindroms = []
for word in wordList:
    if isPalindrom(word):
        palindroms.append(word)

print("palindroms are ", palindroms)