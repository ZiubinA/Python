from functools import reduce
users = [
    {"name": "Jonas", "age": 30},
    {"name": "Petras", "age": 25},
    {"name": "Darius", "age": 40}
]

sorted_users = sorted(users, key=lambda x: x["age"])

raw_data = ["  100 ", "200", "invalid", " 50 "]

cleaned = map(lambda x: x.strip(), raw_data)

valid = filter(lambda x: x.isdigit(), cleaned)

integers = map(int, valid)

total = reduce(lambda x, y: x + y, integers)

print(total) 

print("Task 1: The Multi-Key Sort", '\n')
products = [
    {"name": "Mouse", "category": "Electronics", "price": 20},
    {"name": "Monitor", "category": "Electronics", "price": 200},
    {"name": "T-Shirt", "category": "Clothing", "price": 15},
    {"name": "Laptop", "category": "Electronics", "price": 1000},
    {"name": "Jeans", "category": "Clothing", "price": 40}
]

sorted_products = sorted(products, key=lambda x: (x["category"], -x["price"]))
print(sorted_products)

print('\n', "Task 2: The Map-Reduce Revenue Calculator")

orders = [
    (101, 1, "$100.00"),
    (102, 2, "$50.50"),
    (103, 1, "$20.00")
]

cleaned_amounts = map(lambda order: float(order[2].replace('$', '')), orders)

total_revenue = reduce(lambda acc, val: acc + val, cleaned_amounts)

print(total_revenue) 

print("Task 3: Safe Parsing (The Try-Except Function)")

raw_values = ["10.5", "invalid", "20", "error", "5.5"]

def safe_float(value):
    try:
        value = float(value)

    except:
        return 0.0
    return value

cleaned_values = map(safe_float, raw_values)

total = reduce(lambda x, y: x + y, cleaned_values)

print(total)

print("Task 4: Log Analysis Pipeline")

logs = [
    "INFO: 2023-01-01 User1 Login",
    "ERROR: 2023-01-01 Db Connection Failed",
    "WARNING: 2023-01-01 Disk full",
    "ERROR: 2023-01-01 Timeout"
]

splited_logs = map(lambda x: x.split(' '), logs)
filtered_logs = filter(lambda x: x[0] == "ERROR:", splited_logs)
count_errors = reduce(lambda acc, val: acc + 1, filtered_logs, 0)

print(count_errors)