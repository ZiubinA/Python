new_users = [102, 105, 110, 102, 115, 120] 
banned_users = [105, 120, 199]

dict = {}

for num in new_users:
    if num not in banned_users:
        if num in dict:
            dict[num] += 1
        else:
            dict[num] = 1
print(dict)
print(len(dict))
new_users_set = set(new_users)
banned_users_set = set(banned_users)

valid_users = new_users_set - banned_users_set

print(len(valid_users))
print(valid_users)

print("start task 2", '\n')
visitors = ["192.168.1.1", "10.0.0.1", "192.168.1.1", "172.16.0.5", "10.0.0.1"]
whitelist = ["10.0.0.1", "10.0.0.2"]

list = []

for visitor in visitors:
    if visitor not in whitelist:
        list.append(visitor)
        whitelist.append(visitor)
print("solving using list")
print(len(list))
print(list)

visitors = ["192.168.1.1", "10.0.0.1", "192.168.1.1", "172.16.0.5", "10.0.0.1"]
whitelist = ["10.0.0.1", "10.0.0.2"]

dict = {}
for visitor in visitors:
    if visitor not in whitelist:
        if visitor in dict:
            dict[visitor] += 1
            
        else:
            whitelist.append(visitor) 
            dict[visitor] = 1

print("solving using dictionary", '\n')
print(dict)
print(whitelist)

visitors1 = ["192.168.1.1", "10.0.0.1", "192.168.1.1", "172.16.0.5", "10.0.0.1"]
whitelist1 = ["10.0.0.1", "10.0.0.2"]
visitors_set = set(visitors1)
whitelist_set = set(whitelist1)
new_visitors  = visitors_set - whitelist_set

print("solving using set", '\n')
print(len(new_visitors))
print(new_visitors)

print("start task 3n", '\n')

warehouse_1 = {"apple": 100, "banana": 50, "orange": 20}
warehouse_2 = {"apple": 50, "grape": 30, "banana": 10}

dict = {}
for key, values in warehouse_1.items():
    if key in warehouse_2:
        values += warehouse_2.get(key)
    if key not in dict:
        dict[key] = values

print(dict)

print("start task 4")

raw_sales = [
    (1, 120.50, "USD"),
    (2, 50.00, "USD"),
    (3, 200.00, "EUR"),
    (4, 99.99, "USD"),
    (5, 150.00, "USD"),
]

list = []
for value in raw_sales:
    if value[1] > 100:
        list.append(value[1])
print(list)

number = 1
dict = {}
for value in raw_sales:
    if value[1] > 100 and values[1] == "USD":
        dict[value[1]] = number
        number += 1
print(dict)