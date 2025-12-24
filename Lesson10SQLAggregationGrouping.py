import sqlite3
import pandas as pd

# Setup (Same as before)
conn = sqlite3.connect(":memory:")
df = pd.DataFrame({
    "dept": ["IT", "IT", "HR", "Sales", "Sales", "IT"],
    "salary": [2000, 2200, 1500, 1800, 1900, 3000]
})
df.to_sql("employees", conn, index=False, if_exists="replace")

# Helper
def run_query(q): return pd.read_sql(q, conn)

# Example: Get total company salary cost
print(run_query("SELECT SUM(salary) FROM employees"))

#This is exactly like df.groupby("dept").sum().
#It groups rows that have the same value in a specific column.
#
#Syntax:
#
#SELECT category_column, SUM(target_column)
#FROM table_name
#GROUP BY category_column;

#Example: Average salary per Department.
#
#SELECT dept, AVG(salary) as avg_salary
#FROM employees
#GROUP BY dept;

#3. WHERE vs. HAVING (The Interview Question)
#
#This is the #1 mistake beginners make.
#
#WHERE: Filters Rows (Before grouping).
#
#Example: "Only look at employees named 'Jonas'."
#
#HAVING: Filters Groups (After grouping).
#
#Example: "Only show Departments where the average salary is > 2000."
#
#Wrong:
#SELECT dept, AVG(salary) FROM employees GROUP BY dept WHERE AVG(salary) > 2000 (Error!)
#
#Correct:
#
#SELECT dept, AVG(salary) 
#FROM employees 
#GROUP BY dept 
#HAVING AVG(salary) > 2000;

data = {
    "order_id": [1, 2, 3, 4, 5, 6, 7],
    "customer": ["Jonas", "Petras", "Jonas", "Darius", "Petras", "Jonas", "Darius"],
    "amount": [100, 50, 200, 300, 50, 10, 150],
    "status": ["Completed", "Completed", "Pending", "Completed", "Refunded", "Completed", "Completed"]
}
df = pd.DataFrame(data)

conn = sqlite3.connect(":memory:")
df.to_sql("orders", conn, index=False, if_exists="replace")

def run_query(q): return pd.read_sql(q, conn)

query = "SELECT customer, SUM(amount) as sum, COUNT(customer) as count" \
        " FROM orders " \
        "GROUP BY customer;"
print("\n", run_query(query))

query = "SELECT customer, SUM(amount) FROM orders GROUP BY customer HAVING SUM(amount) > 250;"
print("\n", run_query(query))

query = "SELECT customer, AVG(amount) as avg FROM orders WHERE status LIKE 'Completed' GROUP BY customer;"
print("\n", run_query(query))

query = "SELECT customer, COUNT(*) as count FROM orders GROUP BY customer ORDER BY count DESC"
print("\n", run_query(query))

#How do you count only "Completed" orders vs "Refunded" orders in one row per customer?
#We use CASE WHEN inside the SUM or COUNT function.
#
#SELECT 
#    customer,
#    -- If status is completed, add 1, else add 0. Then Sum it up.
#    SUM(CASE WHEN status = 'Completed' THEN 1 ELSE 0 END) as successful_orders,
#    SUM(CASE WHEN status = 'Refunded' THEN 1 ELSE 0 END) as refunds
#FROM orders
#GROUP BY customer;
#
#If you have a date 2023-01-15 and want to group by Month, you modify the column in the GROUP BY.
#In SQLite, we use substr(date_col, 1, 7) to get '2023-01'.
#
#SELECT 
#    substr(order_date, 1, 7) as month, 
#    SUM(amount) as revenue
#FROM orders
#GROUP BY substr(order_date, 1, 7);

data_adv = {
    "order_id": [1, 2, 3, 4, 5, 6, 7, 8],
    "date": ["2023-01-05", "2023-01-15", "2023-02-01", "2023-02-20", "2023-01-10", "2023-03-01", "2023-01-25", "2023-02-05"],
    "customer": ["Jonas", "Petras", "Jonas", "Darius", "Petras", "Jonas", "Darius", "Jonas"],
    "amount": [100, 50, 200, 300, 50, 10, 150, 20],
    "status": ["Completed", "Completed", "Pending", "Completed", "Refunded", "Completed", "Completed", "Refunded"]
}
df_adv = pd.DataFrame(data_adv)

conn = sqlite3.connect(":memory:")
df_adv.to_sql("orders", conn, index=False, if_exists="replace")

def run_query(q): return pd.read_sql(q, conn)

query = "SELECT customer, (SUM(CASE WHEN status = 'Completed' THEN 1.0 ELSE 0.0 END) / COUNT(*)) * 100 as completion_perceteg FROM orders GROUP BY customer;"
print("\n", run_query(query))

query = "SELECT substr(date, 1, 7) as month, SUM(amount) as revenue FROM orders GROUP BY substr(date, 1, 7);"
print("\n", run_query(query))

query = "SELECT customer, COUNT(*) as order_count, AVG(amount) as average" \
        " FROM orders " \
        " GROUP BY customer" \
        " HAVING order_count > 2 AND average > 50;"
print("\n", run_query(query))