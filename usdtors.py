
USD_TO_INR = 83

def convert_to_inr(products):

    return list(map(lambda p: (p[0], p[1] * USD_TO_INR), products))


def filter_expensive_products(products_in_inr, threshold=3000):

    return list(filter(lambda p: p[1] > threshold, products_in_inr))


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
