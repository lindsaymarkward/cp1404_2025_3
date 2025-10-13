"""
Seminar 3
Task 1 - read file # lines
"""

# filename = input("Enter Filename: ")
# with open(filename) as in_file:
#     for line in in_file:
#         # print(f"!!! {line} {line.startswith("#")}")
#         if line.strip().startswith("#"):
#             print(line.strip())
# print("Finished")

strings = ['Bob', 'Liam', 'This', 'is']
for i, string in enumerate(strings, 1):
    with open(string, "w") as outfile:
        print(i, string, file=outfile)
