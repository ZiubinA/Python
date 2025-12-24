import pandas as pd
import sqlite3

#Scenario: Find the average salary of "High Earners" (salary > 5000).
#
#-- Define the temporary table 'high_earners' first
#WITH high_earners AS (
#    SELECT * FROM employees WHERE salary > 5000
#)
#
#-- Now query it like a real table
#SELECT dept_id, AVG(salary) 
#FROM high_earners 
#GROUP BY dept_id;

#3. Ranking (RANK, DENSE_RANK, ROW_NUMBER)
#
#Scenario: Find the "Top 3 highest paid employees per department".

conn = sqlite3.connect(":memory:")

df = pd.DataFrame({
    "dept": ["IT", "IT", "IT", "HR", "HR"],
    "name": ["Jonas", "Petras", "Darius", "Ruta", "Egle"],
    "salary": [3000, 3000, 2000, 1500, 1800]
})
df.to_sql("employees", conn, index=False, if_exists="replace")

def run_query(q): return pd.read_sql(q, conn)

q = """
SELECT dept, name, salary,
    -- Rank employees by salary within their department
    RANK() OVER (PARTITION BY dept ORDER BY salary DESC) as rank
FROM employees
"""
print(run_query(q))

# Result for IT:
# Jonas  3000  Rank 1
# Petras 3000  Rank 1 (Tie!)
# Darius 2000  Rank 3 (Skips 2 because of tie)

#Scenario: Calculate Month-over-Month Growth. You need to peek at the previous month's sales on the current row.
#
#LAG(col, 1): Value from 1 row before.
#
#LEAD(col, 1): Value from 1 row ahead.

sales = pd.DataFrame({
    "month": ["Jan", "Feb", "Mar"],
    "revenue": [100, 120, 150]
})
sales.to_sql("sales", conn, index=False, if_exists="replace")

q = """
SELECT month, revenue,
    -- Look at previous row's revenue
    LAG(revenue, 1) OVER (ORDER BY rowid) as prev_month_revenue
FROM sales
"""
print(run_query(q))
# Jan: 100, prev: NULL
# Feb: 120, prev: 100
# Mar: 150, prev: 120


conn = sqlite3.connect(":memory:")

data = {
    "emp_id": [1, 2, 3, 4, 5, 6],
    "dept": ["Sales", "Sales", "Sales", "IT", "IT", "IT"],
    "name": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"],
    "salary": [5000, 4000, 6000, 7000, 7200, 5000]
}
df = pd.DataFrame(data)
df.to_sql("staff", conn, index=False, if_exists="replace")

def run_query(q): return pd.read_sql(q, conn)

print("\n Start Tasks\n")

query = "SELECT name, dept, salary, " \
        "RANK() OVER (PARTITION BY dept ORDER BY salary DESC) " \
        "FROM staff"
print("\n Task1", run_query(query))

print("\n Task2")
query = "WITH RankedStaff AS " \
        "( SELECT dept, name, salary, " \
        "DENSE_RANK() OVER (PARTITION BY dept ORDER BY salary DESC) as rnk FROM staff) " \
        "SELECT dept, name, salary " \
        "FROM RankedStaff WHERE rnk = 2"

print(run_query(query))

print("\n Task3")
query = "SELECT name, salary, LEAD(salary) " \
        "OVER (ORDER BY salary DESC) as next_lower_salary, " \
        "salary - LEAD(salary) OVER (ORDER BY salary DESC) as diff FROM staff"
print(run_query(query))

query_4 = "SELECT emp_id, name, salary, SUM(salary) " \
          "OVER (ORDER BY emp_id) as running_total " \
          "FROM staff"
print("\nTask 4")
print(run_query(query_4))