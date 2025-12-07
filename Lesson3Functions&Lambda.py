prices = [100, 200, 300]

discounted = list(map(lambda x: x * 0.9, prices))

print(discounted) 

users = [("Jonas", 30), ("Petras", 25), ("Darius", 40)]

users.sort(key=lambda x: x[1]) 
print(users) 

ages = [15, 22, 10, 45]

adults = list(filter(lambda x: x >= 18, ages))

print(adults)

print("Task 1: The String Cleaner (Map + Lambda)", '\n')

emails = ["  Jonas@Gmail.com", "PETRAS@yahoo.com  ", "darius@gmail.com"]

clear_emails = list(map(lambda email: email.lower().strip(), emails))
print(clear_emails, '\n')

print("Task 2: The Data Filter (Filter + Lambda)", '\n')

transactions = [
    (1, 100, "Completed"),
    (2, 20, "Completed"),
    (3, 200, "Pending"),
    (4, 60, "Completed")
]

transactions_filtered = list(filter(lambda temp: temp[1] > 50 and temp[2] == "Completed", transactions))

print(transactions_filtered)

print("Task 3: Custom Transformation (Pure Function)", '\n')
dates = ["2025-01-01", "2023-12-25", "2024-05-10"]

def parse_date(date_str):
    # Split string by "-" and convert parts to int
    date_str = [int(date) for date in date_str.split('-')]
    return tuple(date_str)

dates_converted = list(map(parse_date, dates))
print(dates_converted)