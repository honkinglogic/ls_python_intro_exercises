#Python offers multiple ways to format strings. The str.format method is a popular method, but since Python 3.6, a new way called f-strings (formatted string literals) was introduced. F-strings offer a concise way to embed expressions inside string literals.

#Given the following variables:

name = "Victor"
profession = "programmer"

print(f'Hello, {name}, you are a {profession}.')

print("Hello, {0}, you are a {1}.".format("Victor", "programmer"))

print('Hello, {}, you are a {}'.format(name, profession))

#How can you print the string Hello, Victor. You are a programmer. using the str.format method? You should fill in the name and profession in a string literal that contains the rest of the text.
#How can you achieve the same result using an f-string?
#Refer to the Python documentation on Format String Syntax and Formatted string literals for guidance.

