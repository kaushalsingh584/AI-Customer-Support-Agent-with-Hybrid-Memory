import sqlite3

conn = sqlite3.connect("../data/orders.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id TEXT PRIMARY KEY,
    status TEXT,
    days_since_delivery INTEGER,
    refund_allowed INTEGER
)
""")

orders = [
    ("ORD123", "Delivered", 3, 1),
    ("ORD456", "Delivered", 10, 0),
    ("ORD789", "Processing", 0, 0)
]

cursor.executemany(
    "INSERT OR REPLACE INTO orders VALUES (?, ?, ?, ?)",
    orders
)

conn.commit()
conn.close()

print("Orders database updated!")