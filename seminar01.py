"""
get number_of_students, number_of_gifts
print number_of_gifts // number_of_students
print number_of_gifts % number_of_students
"""

# number_of_students = int(input("Number of students: "))
# number_of_gifts_total = int(input("Number of gifts: "))
# number_of_gifts_received_each = number_of_gifts_total // number_of_students
# print(f"Each student gets {number_of_gifts_received_each} gifts.")
# print(f"There are {number_of_gifts_total % number_of_students} gifts left over.")

item_price = float(input("Item price: "))
whether_has_gst = input("Haz GST (y/n): ").upper()
if whether_has_gst == "Y":
    item_price *= 1.1
print(f"Final price is {item_price:.2f}")

