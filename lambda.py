customers = [
    {"name": "A", "purchases": [50, 200, 300], "active": True},
    {"name": "B", "purchases": [500, 20], "active": False},
    {"name": "C", "purchases": [150, 250], "active": True}
]

def calculate_total_revenue(customers):
    tax = lambda x: x * 1.10
    is_valid = lambda x: x >= 100

    # Filter active customers
    active_customers = filter(lambda c: c["active"], customers)

    # Process purchases
    total = sum(
        map(
            tax,
            filter(
                is_valid,
                [amount for c in active_customers for amount in c["purchases"]]
            )
        )
    )

    return total


print(calculate_total_revenue(customers))
