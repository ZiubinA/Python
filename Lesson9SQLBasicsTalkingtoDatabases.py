import sqlite3
import pandas as pd

# 1. Create a connection to an in-memory database
conn = sqlite3.connect(":memory:")

# 2. Upload a DataFrame to the database (so we have data to query)
df = pd.DataFrame({"name": ["Jonas", "Petras"], "age": [30, 25]})
df.to_sql("users", conn, index=False, if_exists="replace")

# 3. Run a Query
query = "SELECT * FROM users"
result = pd.read_sql(query, conn)

print(result)

#SELECT * FROM users WHERE name LIKE 'J%'; -- Starts with J
#SELECT * FROM users WHERE name LIKE '%as'; -- Ends with as

#-- Ascending (Default)
#SELECT * FROM users ORDER BY age;
#
#-- Descending
#SELECT * FROM users ORDER BY age DESC;

#-- Show top 5 oldest users
#SELECT * FROM users ORDER BY age DESC LIMIT 5;

#Equivalent to df['col'].unique().
#
#SELECT DISTINCT city FROM users;


# Create Data
data = {
    "id": [1, 2, 3, 4, 5, 6],
    "name": ["Laptop", "Mouse", "Monitor", "Keyboard", "Phone", "Cable"],
    "category": ["Tech", "Accessories", "Tech", "Accessories", "Tech", "Accessories"],
    "price": [1200, 20, 300, 50, 800, 10],
    "stock": [5, 0, 10, 20, 8, 50]
}
df = pd.DataFrame(data)

# Connect & Upload
conn = sqlite3.connect(":memory:")
df.to_sql("products", conn, index=False, if_exists="replace")

# Helper function to run queries
def run_query(q):
    return pd.read_sql(q, conn)

query = "SELECT name, price FROM products"
result = run_query(query)
print("\n", result)

query = "SELECT * FROM products WHERE category LIKE 'Tech' AND price > 500"
result = run_query(query)
print("\n", result)

query = "SELECT * FROM products ORDER BY price DESC LIMIT 3"
result = run_query(query)
print("\n", result)

query = "SELECT * FROM products WHERE name LIKE 'M%'"
result = run_query(query)
print("\n", result)

query = "SELECT DISTINCT category FROM products"
result = run_query(query)
print("\n", result)

#You can create new columns on the fly inside the query.
#
#-- Calculate 'Total Value' (Price * Stock) and rename it to 'potential_revenue'
#SELECT name, price * stock as potential_revenue FROM products;

#Instead of writing WHERE category='A' OR category='B' OR category='C', use IN.
#
#SELECT * FROM products WHERE category IN ('Tech', 'Gaming', 'Office');

#Instead of WHERE price >= 100 AND price <= 500, use BETWEEN.
#
#SELECT * FROM products WHERE price BETWEEN 100 AND 500;

#Just like in Python, AND happens before OR. Use parentheses to force order.
#
#-- Wrong: Might return cheap accessories if logic is mixed up
#SELECT * FROM products WHERE category = 'Tech' OR category = 'Office' AND price > 100;
#
#-- Correct: (Tech OR Office) AND Price > 100
#SELECT * FROM products WHERE (category = 'Tech' OR category = 'Office') AND price > 100;

query = "SELECT name, category, price * stock as potential_revenue" \
        " FROM products " \
        "ORDER BY potential_revenue DESC;"
result = run_query(query)
print("\n", result)

query = "SELECT * FROM products WHERE category LIKE 'Tech' AND price BETWEEN 50 AND 500;"
result = run_query(query)
print("\n", result)

query = "SELECT * FROM products WHERE stock = 0 OR (stock < 20 AND category LIKE 'Accessories');"
result = run_query(query)
print("\n", result)

query = "SELECT * FROM products WHERE name IN('Mouse', 'Keyboard', 'Webcam');"
result = run_query(query)
print("\n", result)