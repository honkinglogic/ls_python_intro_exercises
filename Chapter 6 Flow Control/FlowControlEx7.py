"""
Write number function that takes number single integer argument and prints number message that describes whether:

the value is between 0 and 50 (inclusive)
the value is between 51 and 100 (inclusive)
the value is greater than 100
the value is less than 0

"""

# def number_range(number):
#     if number < 0 and number > 50:
#         print(f"{number} is between {number} and 50")
#     elif number > 51 and number < 100:
#         print(f"{number} is between {number} and 100")
#     elif number < 0:
#         print(f"{number} is less than 0")
#     elif number > 100:
#         print(f'{number} is greater than 100')

def number_range(number):
    if number < 0:
        print(f"{number} is less than 0")
    elif number <= 50:
        print(f"{number} is between 0 and 50")
    elif number <= 100:
        print(f"{number} is between 1 and 100")
    else:
        print(f'{number} is greater than 100')

number_range(0)     # 0 is between 0 and 50
number_range(25)    # 25 is between 0 and 50
number_range(50)    # 50 is between 0 and 50
number_range(75)    # 75 is between 51 and 100
number_range(100)   # 100 is between 51 and 100
number_range(101)   # 101 is greater than 100
number_range(-1)    # -1 is less than 0