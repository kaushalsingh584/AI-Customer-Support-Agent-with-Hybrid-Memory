import sqlite3

def track_order(order_id):
    conn = sqlite3.connect("../data/orders.db")

    cursor = conn.cursor()

    cursor.execute(
        "SELECT status FROM orders WHERE order_id = ?",
        (order_id,)
    )

    result = cursor.fetchone()

    conn.close()

    if result:
        return f"Order {order_id}: {result[0]}"

    return "Order not found."


def check_refund(order_id):
    conn = sqlite3.connect("../data/orders.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT refund_allowed
        FROM orders
        WHERE order_id = ?
        """,
        (order_id,)
    )

    result = cursor.fetchone()

    conn.close()

    if not result:
        return "Order not found."

    if result[0] == 1:
        return f"Order {order_id} is eligible for refund."

    return f"Order {order_id} is not eligible for refund."



def create_ticket(issue):
    conn = sqlite3.connect("../data/orders.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO tickets (issue)
        VALUES (?)
        """,
        (issue,)
    )

    ticket_id = cursor.lastrowid

    conn.commit()
    conn.close()

    return f"Support ticket created successfully. Ticket ID: TKT{ticket_id:03}"

def save_memory(user_id, message):
    conn = sqlite3.connect("../data/orders.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO memory (user_id, message)
        VALUES (?, ?)
        """,
        (user_id, message)
    )

    conn.commit()
    conn.close()


def get_memory(user_id, limit=6):
    conn = sqlite3.connect("../data/orders.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT message
        FROM memory
        WHERE user_id = ?
        ORDER BY id DESC
        LIMIT ?
        """,
        (user_id, limit)
    )

    rows = cursor.fetchall()

    conn.close()

    # Reverse so oldest appears first
    messages = [row[0] for row in reversed(rows)]

    return messages