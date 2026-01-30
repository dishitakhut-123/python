def countListElement(lst):
    output = {}
    for val in lst:
        if val in output:
            output[val] = output[val] + 1
        else:
            output[val] = 1
    return output


def main():
    input2 = [4, 1, 6, 5, 4, 5, 5, 1, 4]
    result = countListElement(input2)
    print(result)


main()
