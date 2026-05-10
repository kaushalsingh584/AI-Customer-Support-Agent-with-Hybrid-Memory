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
