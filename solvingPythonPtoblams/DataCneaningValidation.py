raw_users = [
    {"name": "  Alice  ", "age": 25, "email": "alice@email.com"},
    {"name": "Bob", "age": -5, "email": "bob@email.com"},
    {"name": "Charlie", "age": 30},
    {"name": "  David", "age": None, "email": "david@email.com"},
    {"name": "Eve", "age": 22, "email": "eve@email.com"}
]

cleaned_data = []
    
for user in raw_users:
    if "email" not in user:
        continue

    age = user.get("age")
    if not isinstance(age, int) or age <= 0:
        continue

    if "name" in user:
        user["name"] = user["name"].strip()
        
    cleaned_data.append(user)    
print(cleaned_data)

def fizzBuzz(n):
    i = 1
    while i <= n:
        if i % 5 == 0 and i % 3 == 0:
            i += 1
            return "FizzBuzz"
        elif i % 5 == 0:
            i += 1
            return "Buzz"
        elif i % 3 == 0:
            i += 1
            return "Fizz"
        else:
            print(i)
            i += 1
    
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)







def solvePalindrome(s):
    count = 0
    for char in s:
        count = count + (ord(char) - ord('a') + 1)
        print(count)

s = input()
result = solvePalindrome(s)