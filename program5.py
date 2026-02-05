def check_key(d, key):
    if key in d:
        return "Found"
    else:
        return "Not Found"


def main():
    data = {"a": 1, "b": 2}
    key = "b"
    result = check_key(data, key)
    print(result)


main()
