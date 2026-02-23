

def fizz_bus(x):
    for i in range(1, x + 1):
        if i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 5 == 0 and i % 3 == 0:
            print("FizzBuzz")
        else: print(i)

print("write number")
x = input()
print(fizz_bus(int(x)))        

def isPalindrom(word):
    length = len(word)
    for i in word:
        if i != word[length - 1]:
            return False
        length = length - 1
    return True

print("write word")
word = input()
print(isPalindrom(word))