"""
Script to print the collatz sequence given user input.
"""


def collatz(number):
    """
    Do the Collatz sequence with 'number'. Output is printed and returned.
    """
    if number % 2 == 0:
        print(number // 2)
        return number // 2

    elif number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return result


def main():
    x = int(input("Enter a number: "))

    while x != 1:
        x = collatz(x)


if __name__ == "__main__":
    main()
