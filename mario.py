from cs50 import get_int


def main():

    i = get_number()

    # prints the pyramid using given height
    for layer in range(i + 1):
        if layer == 0:
            pass
        else:
            print(" " * (i - layer) + "#" * layer)  # prints pyramid by each line


# Prompts user for positive integer (1-8 inclusive)
def get_number():

    while True:
        n = get_int("Height: ")
        if n > 0 and n <= 8:
            break
    return n


main()