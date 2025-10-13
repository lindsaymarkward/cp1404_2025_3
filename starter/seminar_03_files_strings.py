# What is the output of the following code?

s = "\tPython, Monty  \n"
print(s[1], ".", sep="")
print(s.strip(), ".", sep="")
s.replace(' ', '*')
print(s.lstrip(), ".", sep="")
print(s.strip().split(','))

# Rewrite the following to use with
name = input("Name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()
print("Done")
