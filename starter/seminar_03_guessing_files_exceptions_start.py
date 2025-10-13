"""Guessing game with files and exceptions"""


def main():
    secret = 6
    guess = int(input("? "))
    while guess != secret:
        print("Guess again!")
        guess = int(input("? "))
    print("You got it!")


# main()

# What exceptions can you create?
# What can you enter to get no errors?

value = int(input("> "))
result = f"{value}" * value
print(result)
thing = result[value]
print(thing)

# What is the output of this code?
try:
    number = input("> ")
    print(int(number + 1))
except ValueError:
    print("Not a valid integer")
except TypeError:
    print("Invalid type of thing")
except:
    print("Some other exception happened")
else:
    print("Else")
print("Finished")
