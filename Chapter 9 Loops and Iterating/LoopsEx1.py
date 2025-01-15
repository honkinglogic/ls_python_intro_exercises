#Modify the age.py program you wrote in Exercise 3 of the Input/Output chapter. The updated code should use a for
# loop to display the future ages.

#Previous question: Write a program named age.py that asks the user to enter their age, then calculates and reports
# the future age 10, 20, 30, and 40 years from now. Here's the output for someone who is 27 years old.
# This solution coerces the input age when a numeric
# age is needed. This code is repetitive.

age = int(input('How old are you? '))
print()
print(f'You are {age} years old.')

for future in range(10, 50, 10):
    print(f'In {future} years, you will be {age + future} years old.')

# print(f'In 10 years, you will be {int(age) + 10} years old.')
# print(f'In 20 years, you will be {int(age) + 20} years old.')
# print(f'In 30 years, you will be {int(age) + 30} years old.')
# print(f'In 40 years, you will be {int(age) + 40} years old.')