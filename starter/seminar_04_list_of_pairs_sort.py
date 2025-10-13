"""
Seminar 04 - Sort and display in columns
"""
from operator import itemgetter

data = [['Derek', 7], ['Xavier', 80], ['Bob', 612], ['Chantanelle', 9]]
max_length = max((len(pair[0]) for pair in data))

for pair in sorted(data, key=itemgetter(1), reverse=True):
    name, score = pair
    print(f"{name:{max_length}} = {score:4}")
print()
