"""Seminar 5 - Dictionaries"""


def main():
    print(convert_to_dictionary(["a", "bbb", "longer string", ""]))
    print(convert_to_dictionary2(["a", "bbb", "longer string", ""]))


def convert_to_dictionary2(strings):
    return {string: len(string) for string in strings}


def convert_to_dictionary(strings):
    string_to_length = {}
    for string in strings:
        string_to_length[string] = len(string)
    return string_to_length


main()
