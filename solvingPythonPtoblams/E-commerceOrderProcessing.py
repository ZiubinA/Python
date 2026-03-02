#Calculate the total revenue (sum of all item prices), but only for orders where the status is "completed".

orders = [
    {"id": 101, "items": [{"price": 10}, {"price": 20}], "status": "completed"},
    {"id": 102, "items": [{"price": 5}, {"price": 5}], "status": "pending"},
    {"id": 103, "items": [{"price": 50}], "status": "canceled"},
    {"id": 104, "items": [{"price": 10}, {"price": 10}, {"price": 10}], "status": "completed"},
    {"id": 105, "items": [], "status": "completed"}
]

total_revenue = 0
for order in orders:
    if order["status"] == "completed":
        for item in order["items"]:
            total_revenue += item["price"]
print(total_revenue)