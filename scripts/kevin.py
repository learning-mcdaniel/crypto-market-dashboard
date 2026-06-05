import sqlite3

conn = sqlite3.connect("data/cypto.db")

cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_schema WHERE type='table' AND name='cypto_prices'")

tables = cursor.fetchall()
for table in tables:
    print(f"Table Name:  {table[0]}")


