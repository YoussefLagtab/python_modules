import sys


def print_usage():
    print("""Usage: python operations.py <number1> <number2>
Example:
    python operations.py 10 3""")


def operations(nb1, nb2):
    print("Sum:", nb1 + nb2)
    print("Difference:", nb1 - nb2)
    print("Product:", nb1 * nb2)
    print("Quotient:", (float(nb1) / nb2) if nb2 != 0 else "ERROR (div by 0)")
    print("Remainder:", (nb1 % nb2) if nb2 != 0 else "ERROR (modulo by 0)")


def main():
    if len(sys.argv) == 1:
        print_usage()
        return

    if len(sys.argv) != 3:
        print('InputError: wrong number of arguments\n')
        print_usage()
        return

    if not sys.argv[1].isnumeric() or not sys.argv[2].isnumeric():
        print("InputError: only numbers\n")
        print_usage()
        return

    nb1 = int(sys.argv[1])
    nb2 = int(sys.argv[2])
    operations(nb1, nb2)


if __name__ == "__main__":
    main()
