#The following function returns a list of the remainders of dividing the numbers in numbers by 5:

def remainders_5(numbers):
    return [number % 5 for number in numbers]

#Use this function to determine which of the following lists do not contain any numbers that are divisible by 5:

numbers_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_2 = [1, 2, 3, 4, 6, 7, 8, 9]
numbers_3 = [0, 5, 10]
numbers_4 = []

#Note: when working with integers, a value of 0 is "falsy"; all other integers are "truthy".

print(all(remainders_5(numbers_1)))  #[0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0] #False (at least one zero)
print(all(remainders_5(numbers_2)))                                     #True (no zeros)
print(all(remainders_5(numbers_3)))                                     #False
print(all(remainders_5(numbers_4)))                                     #True