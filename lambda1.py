products = [
    ("Laptop", "Electronics", 1000),
    ("Shirt", "Clothing", 50),
    ("Phone", "Electronics", 500)
]

def filter_category(products, category):

    return list(filter(lambda p: p[1] == category, products))

def apply_discount(price, discount_rate=0.20):

    return price * (1 - discount_rate)

def total_discounted_price(products, category="Electronics", discount_rate=0.20):

    filtered = filter_category(products, category)
    discounted = map(lambda p: apply_discount(p[2], discount_rate), filtered)
    return sum(discounted)

    
print(total_discounted_price(products))
