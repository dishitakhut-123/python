def count_elements(lst):
    result = {}

    for num in lst:
        if num in result:
            result[num] += 1
        else:
            result[num] = 1

    return result


def main():
    input_list = [1, 2, 2, 3, 3, 3]
    output = count_elements(input_list)
    print(output)


main()
