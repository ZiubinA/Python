#You have a table of Call Data Records (CDRs). Every time someone makes a call, a row is added.
#Your manager wants a list of customers who have spent the most time on the phone.

import sqlite3
import pandas as pd

conn = sqlite3.connect(":memory:")
cur = conn.cursor()

cur.execute("CREATE TABLE customers (id INTEGER, name TEXT, phone_number TEXT)")
cur.execute("CREATE TABLE calls (id INTEGER, phone_number TEXT, duration_seconds INTEGER)")

customers_data = [
    (1, 'Jonas', '+37060000001'),
    (2, 'Petras', '+37060000002'),
    (3, 'Antanas', '+37060000003'),
    (4, 'Ona', '+37060000004')
]

calls_data = [
    (101, '+37060000001', 120),  
    (102, '+37060000001', 60),   
    (103, '+37060000002', 300),  
    (104, '+37060000004', 0),    
    (105, '+37060000001', 500)   
]

cur.executemany("INSERT INTO customers VALUES (?,?,?)", customers_data)
cur.executemany("INSERT INTO calls VALUES (?,?,?)", calls_data)
conn.commit()


sql_query = """ SELECT c.name, c.phone_number, SUM(ca.duration_seconds) as total
FROM customers as c 
INNER JOIN calls as ca ON ca.phone_number = c.phone_number
GROUP BY c.name, c.phone_number ORDER BY total DESC
"""

print(pd.read_sql_query(sql_query, conn))

df = pd.read_sql_query(sql_query, conn)
df['phone_number'] = df['phone_number'].str.replace("+", "")

def clean_prefix(num):
    if num.startswith('86'):
        return '3706' + num[2:] 
    return num

df['phone_number'] = df['phone_number'].apply(clean_prefix)

df['phone_number'].astype(int)
print(df)

