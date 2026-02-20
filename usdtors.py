USD_TO_INR = 83

def convert_to_inr(products):
    converted = []
    for name, price in products:
        converted.append((name, price * USD_TO_INR))
    return converted


def filter_expensive_products(products_in_inr, threshold=3000):
    expensive = []
    for name, price in products_in_inr:
        if price > threshold:
            expensive.append((name, price))
    return expensive


def main():
    products = [
        ("Pen", 10),
        ("Bag", 50),
        ("Shoes", 60)
    ]

    products_in_inr = convert_to_inr(products)
    expensive_products = filter_expensive_products(products_in_inr)

    print("Products costing more than ₹3000:")
    print(expensive_products)


if __name__ == "__main__":
    main()
