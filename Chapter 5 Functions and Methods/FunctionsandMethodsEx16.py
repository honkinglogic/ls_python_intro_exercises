def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

"""

#In the code shown, identify all of the function names and parameters present in the code. Include the line
# numbers for each item identified.

function names: 
- multiply: defined on line 1, used on line 9
- get_num: defined on line4, used on line 7 and line 8
- float: built-in function, used on line 5
- input: built-in function, used on line 5
- print: built-in function, used on line 10

parameters: 
- left, right: defined on line 1, used in line 2




"""
