def check_even_odd():
    start = int(input("Enter the starting number: "))
    end = int(input("Enter the ending number: "))

    for num in range(start, end + 1):
        if num % 2 == 0:
            print(num, "is Even")
        else:
            print(num, "is Odd")


def main():
    check_even_odd()


if __name__ == "__main__":
    main()
