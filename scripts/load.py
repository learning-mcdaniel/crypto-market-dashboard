import sqlite3
import requests

url = (
    "https://api.coingecko.com/api/v3/simple/price"
    "?ids=bitcoin,ethereum"
    "&vs_currencies=usd"
)

data = requests.get(url).json()

conn = sqlite3.connect("data/crypto.db")

cursor = conn.cursor()

for coin, value in data.items():

    cursor.execute("""
    INSERT INTO crypto_prices
    (coin, price)
    VALUES (?,?)
    """,
    (coin, value["usd"])
    )

conn.commit()

conn.close()

print("Data loaded.")

