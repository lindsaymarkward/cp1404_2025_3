"""
What's wrong with this code from practical 03 files, question 4?
How can we improve it?
"""

with open("numbers.txt", "r") as input_file:
    numbers = input_file.readlines()
    sum_of_numbers = 0
    for number in numbers:
        sum_of_numbers += float(number)
    print(f"Total sum of numbers is {sum_of_numbers}")
