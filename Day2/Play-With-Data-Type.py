# TypeError
# len(123) --> To remove this error we need to convert the type before calculating the length i.e, len(str(123))

# No TypeError
len("Hello")

# Type Checking
print(type("abc"))
print(type(123))
print(type(3.14))
print(type(True))


name_of_the_user = input("Enter your name")
length_of_name = len(name_of_the_user)

print(type("Number of letters in your name: "))  # str
print(type(length_of_name))  # int

print("Number of letters in your name: " + str(length_of_name))
