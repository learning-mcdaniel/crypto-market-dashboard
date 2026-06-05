import sqlite3

conn = sqlite3.connect("data/crypto.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS crypto_prices(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    coin TEXT,
    price REAL,
    load_timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()
conn.close()

print("Database created.")
