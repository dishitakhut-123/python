def tuple_to_dict(tuples):
    result = {}

    for key, value in tuples:
        result[key] = value

    return result


def main():
    data = (("a", 1), ("b", 2))
    output = tuple_to_dict(data)
    print(output)


main()
