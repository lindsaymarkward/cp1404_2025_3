from operator import itemgetter

data = [['Derek', 7], ['Xavier', 80], ['Bob', 612], ['Chantanelle', 9]]
# data.sort(reverse=True, key=itemgetter(1, 0))
max_length = max((len(pair[0]) for pair in data))
print(max_length)

for name, score in sorted(data, reverse=True, key=itemgetter(1, 0)):
    print(f"{name:{max_length}} = {score:3}")

# names = ["Ada", "Alan", "Bill", "John"]
# print(", ".join(names))
# name_to_remove = input("Who do you want to remove? ")
# while name_to_remove != "":
#     try:
#         names.remove(name_to_remove)
#     except ValueError:
#         print(f"{name_to_remove} is not in the list")
#     else:
#         print(f"{name_to_remove} removed.")
#     print(", ".join(names))
#     name_to_remove = input("Who do you want to remove? ")
# print("Finished")
