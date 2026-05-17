import re

def route_query(user_query):
    query = user_query.lower()

    # Order / Refund queries
    if "refund" in query:
        return "order_agent"

    if re.search(
        r'ORD\d+',
        user_query.upper()
    ):
        return "order_agent"

    # Escalation queries
    if any(
        phrase in query
        for phrase in [
            "talk to human",
            "talk to agent",
            "raise complaint",
            "create ticket",
            "damaged",
            "i have a problem",
            "damaged product"
        ]
    ):
        return "escalation_agent"

    # Default
    return "faq_agent"