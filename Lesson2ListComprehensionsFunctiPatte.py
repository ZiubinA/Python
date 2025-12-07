numbers = [1, 2, 3, 4, 5]
squared = [x * x for x in numbers] 
print(squared)


temps = [22, 25, -999, 21, -999, 23]
clean_temps = []

for t in temps:
    if t != -999:
        clean_temps.append(t)
print(clean_temps)

clean_temps2 = [t for t in temps if t != -999]

print(clean_temps2)

print("Task Currency Converte")

prices_usd = [100, 50, 20, 10]
rate = 0.92

euro = [i * rate for i in prices_usd]
print(euro, '\n')

print("Task 2: The Data Cleaner")

raw_names = ["  joNas ", "PETRAS", "   darius", "Adomas  "]
clean_names = [name.title().strip() for name in raw_names] 

print(clean_names, '\n')

print("Task 3: The Filter", '\n')

transactions = [50, 1200, 40, 5000, 25]

filtered = [num for num in transactions if num < 1000]
print(filtered)

print("practice with tuples")
users = [
    (101, "Jonas", "Admin"),
    (102, "Petras", "User"),
    (103, "Darius", "User")
]

names = [u[1] for u in users] 
print(names)

names2 = [names for user_id, names, role in users]
print(names2)

print("using zip")
products = ["Apple", "Banana", "Cherry"]
prices = [1.2, 0.5, 2.5]

price_map = {prod: price for prod, price in zip(products, prices)}
print(price_map)

batches = [
    [101, 102],
    [103, 104, 105],
    [106]
]

all_ids = [t_id for batch in batches for t_id in batch]

print(all_ids)


print("Task 1: The Invoice Calculator (Tuple Unpacking)", '\n')

invoice_items = [
    ("Laptop", 1, 800.00),
    ("Mouse", 2, 25.50),
    ("Monitor", 2, 150.00),
    ("HDMI Cable", 5, 10.00)
]

line_totals = [quantity * price for name, quantity, price in invoice_items ]
print(line_totals)

print("Task 2: The High Value Filter (Tuples + If)")

totals_more100 = [quantity * price for name, quantity, price in invoice_items if quantity * price > 100]
print(totals_more100)

print("Task 3: Combining Data (Zip + Dict Comprehension)")

students = ["Jonas", "Adomas", "Ruta", "Benas"]
scores = [95, 78, 88, 60]

top_students = {name: price for name, price in zip(students, scores)}
print(top_students)

print("Task 4: Matrix Flattening (Nested)")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

odd_numbers = [odd_number for numbers in matrix for odd_number in numbers if odd_number % 2 != 0]
print(odd_numbers)