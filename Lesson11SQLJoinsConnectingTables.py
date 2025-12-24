import pandas as pd
import sqlite3

#In Pandas, you wrote:
#pd.merge(users, orders, on="user_id", how="left")
#
#In SQL, you write:
#
#SELECT * FROM users 
#LEFT JOIN orders ON users.user_id = orders.user_id;

import sqlite3
import pandas as pd

conn = sqlite3.connect(":memory:")

users = pd.DataFrame({
    "user_id": [1, 2, 3],
    "name": ["Jonas", "Petras", "Darius"],
    "role": ["Admin", "User", "User"]
})

orders = pd.DataFrame({
    "order_id": [101, 102, 103, 104],
    "user_id": [1, 1, 2, 99], # Note: User 99 does not exist in 'users'
    "amount": [50, 100, 25, 200]
})

users.to_sql("users", conn, index=False, if_exists="replace")
orders.to_sql("orders", conn, index=False, if_exists="replace")

def run_query(q): return pd.read_sql(q, conn)

#Keeps only rows where the ID exists in BOTH tables.
#User 99 (Order 104) is dropped. Darius (User 3) is dropped.
#
#q = """
#SELECT users.name, orders.amount 
#FROM users 
#INNER JOIN orders ON users.user_id = orders.user_id
#"""
#print(run_query(q))

#Keeps everything from the Left table (users).
#Darius is kept (amount is NaN/Null). User 99 is still dropped (because he is on the Right).
#
#q = """
#SELECT users.name, orders.amount 
#FROM users 
#LEFT JOIN orders ON users.user_id = orders.user_id
#"""
#print(run_query(q))

#"How much did each User spend in total?"
#
#Join users and orders.
#
#Group By users.name.
#
#Sum orders.amount.
#
#q = """
#SELECT users.name, SUM(orders.amount) as total_spent
#FROM users
#LEFT JOIN orders ON users.user_id = orders.user_id
#GROUP BY users.name
#"""
#print(run_query(q))

conn = sqlite3.connect(":memory:")

employees = pd.DataFrame({
    "emp_id": [10, 20, 30, 40],
    "name": ["Alice", "Bob", "Charlie", "David"],
    "dept_id": [1, 1, 2, 99] # David is in unknown dept 99
})

departments = pd.DataFrame({
    "dept_id": [1, 2, 3],
    "dept_name": ["IT", "HR", "Sales"]
})

employees.to_sql("employees", conn, index=False, if_exists="replace")
departments.to_sql("departments", conn, index=False, if_exists="replace")

def run_query(q): return pd.read_sql(q, conn)

query = "SELECT employees.name, departments.dept_name " \
        "FROM employees " \
        "LEFT JOIN departments ON employees.dept_id = departments.dept_id"

print(run_query(query))

query = "SELECT departments.dept_name, employees.name " \
    "FROM departments " \
    "LEFT JOIN employees ON employees.dept_id = departments.dept_id " \
    "WHERE employees.emp_id IS NULL"
print(run_query(query))

query = "SELECT departments.dept_name, employees.name, COUNT(employees.name) as employees_count " \
        "FROM departments " \
        "LEFT JOIN employees ON departments.dept_id = employees.emp_id " \
        "GROUP BY departments.dept_name"
print(run_query(query))

query = "SELECT employees.name, departments.dept_name " \
        "FROM departments " \
        "LEFT JOIN employees ON employees.dept_id = departments.dept_id " \
        "WHERE departments.dept_name = 'IT'"

print(run_query(query))

import sqlite3
import pandas as pd

conn = sqlite3.connect(":memory:")

# 1. Create DataFrames
products = pd.DataFrame({
    "product_id": [1, 2, 3, 4, 5],
    "product_name": ["Laptop", "Mouse", "Monitor", "Desk Chair", "Old Cable"],
    "category_id": [10, 10, 10, 20, 99], # Note: 99 does not exist in categories
    "price": [1000, 25, 200, 150, 5]
})

categories = pd.DataFrame({
    "category_id": [10, 20, 30],
    "category_name": ["Electronics", "Furniture", "Clothing"]
})

# 2. Upload to SQL
products.to_sql("products", conn, index=False, if_exists="replace")
categories.to_sql("categories", conn, index=False, if_exists="replace")

def run_query(q): 
    return pd.read_sql(q, conn)

print("Setup Complete! Tables 'products' and 'categories' are ready.")

print("\n Task 1 Basic Joins\n")

query = "SELECT products.product_name, categories.category_name " \
        "FROM products " \
        "LEFT JOIN categories ON categories.category_id = products.category_id"
print("\n", run_query(query))

print("\n Task 2")
query = "SELECT products.product_name, categories.category_name " \
        "FROM products " \
        "LEFT JOIN categories ON categories.category_id = products.category_id " \
        "WHERE categories.category_name IS NULL"
print("\n", run_query(query))

print("\n Task 3: Aggregation (Counting)")
query = "SELECT products.product_name, categories.category_name, COUNT(products.product_id) as product_count " \
        "FROM products " \
        "LEFT JOIN categories ON categories.category_id = products.category_id " \
        "GROUP BY categories.category_name " \
        
print("\n", run_query(query))

print("\n Task 4: Aggregation (Summing Money)")
query = "SELECT categories.category_name, SUM(products.price) as peoduct_price " \
        "FROM categories " \
        "LEFT JOIN products ON products.category_id = categories.category_id " \
        "GROUP BY categories.category_name HAVING peoduct_price > 100"
print("\n", run_query(query))