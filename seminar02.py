"""
<priming read - get some input>
while <input is bad>
    display error message
    <same as the priming read again - get some input>
do next thing now that you know the input is valid
"""
from random import randint


def main():
    """Docstring."""
    print("Hello")
    do_random_number()
    # that's it


def do_random_number():
    # Get boundaries
    low = int(input("Low: "))
    high = int(input("High: "))
    while low >= high:
        print("Error")
        high = int(input("High: "))
    print(":) " * randint(low, high))


main()
