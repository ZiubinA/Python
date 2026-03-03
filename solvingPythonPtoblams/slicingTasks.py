def extractSufix(s):
    newword = ""
    for i in s:
        if s.index(i) == 0:
            newword += i
            continue
        elif i.islower():
            newword += i
        elif i.isupper():
            return newword

word = "JavaScript"
newWord = extractSufix(word)
print(newWord)

def extractSufixSlicing(s):
    for i in range(1, len(s)):
        if s[i].isupper():
            return s[:i]

print(extractSufixSlicing(word))

def extractWord(s):
    word = ""
    for i in range(0, len(s), 2):
        word += s[i]
    return word

print(extractWord("Hxeolclboo"))

def extractWordSlicing(s):
    word = ""

    word += s[::2] 
    return word

print(extractWordSlicing("Hxeolclboo"))