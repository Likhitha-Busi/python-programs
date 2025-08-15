#remove space from a given string
text = input("Enter  a string: ")
no_space = ""
for char in text:
    if char != " ":
        no_space += char
print("String without spaces:", no_space)
