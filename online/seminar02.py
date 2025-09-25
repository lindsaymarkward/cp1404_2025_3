"""
<priming read - get some input>
while <input is bad>
    display error message
    <same as the priming read again - get some input>
do next thing now that you know the input is valid
"""
from random import randint


def main():
    low, high = get_limits()
    print(randint(low, high))


def get_limits() -> tuple[int, int]:
    low = int(input("Low: "))
    high = int(input("High: "))
    while low >= high:
        print(f"Invalid. High number must be > {low}")
        high = int(input("High: "))
    return low, high


if __name__ == '__main__':
    main()
