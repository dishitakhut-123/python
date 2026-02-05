def reverse_words(s):
    words = s.split()
    reversed_words = words[::-1]
    return reversed_words


def main():
    text = "data science is fun"
    output = reverse_words(text)
    print(output)


main()
