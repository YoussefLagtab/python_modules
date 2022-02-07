import sys


def operations(nb1, nb2):
    print("Sum:", nb1 + nb2)
    print("Difference:", nb1 + nb2)
    print("Product:", nb1 + nb2)
    print("Quotient:", float(nb1) / nb2)
    print("Remainder:", nb1 % nb2)


def main():
    if len(sys.argv) != 3:
        print('ERROR')
        return
    nb1 = int(sys.argv[1])
    nb2 = int(sys.argv[2])
    operations(nb1, nb2)


if __name__ == "__main__":
    main()
