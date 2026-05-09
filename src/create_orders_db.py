import sqlite3

conn = sqlite3.connect("../data/orders.db")

cursor = conn.cursor()

# Create orders table
cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id TEXT PRIMARY KEY,
    status TEXT
)
""")

# Insert sample orders
orders = [
    ("ORD123", "Out for delivery"),
    ("ORD456", "Delivered"),
    ("ORD789", "Processing")
]

cursor.executemany(
    "INSERT OR REPLACE INTO orders VALUES (?, ?)",
    orders
)

conn.commit()
conn.close()

print("Orders database created successfully!")