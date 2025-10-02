"""
Write a program to read a file and print ONLY the lines that start with a #
The user should enter the filename.
"""

# filename = input("Filename: ")
filename = "seminar02.py"
with open(filename, "r") as in_file:
    lines = in_file.readlines()
    in_file.read()
for line in lines:
    if line.lstrip().startswith("#"):
        # print("inside the if")
        print(line.rstrip())

"""
Write code that creates files from a list of strings.
Each file should be named with the value of the string with a .txt extension. If the string is "Bob", create a file called "Bob.txt".
Write the string to the file.

Version 2:
Write the position in the list to the file, starting from 1.
"""
strings = ["Bob", "thisisanotherone", "here"]
for i, string in enumerate(strings, 1):
    filename = f"{string}.txt"
    print(i, filename)
    with open(filename, "w") as out_file:
        print(i, file=out_file)
