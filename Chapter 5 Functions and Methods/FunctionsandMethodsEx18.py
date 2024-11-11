#The following function returns a list of the remainders of dividing the numbers in numbers by 3:#
def remainders_3(numbers):
    return [number % 3 for number in numbers]

#Use this function to determine which of the following lists contains at least one number that is not evenly divisible
# by 3 (that is, the remainder is not 0):

numbers_1 = [0, 1, 2, 3, 4, 5, 6]
numbers_2 = [1, 2, 4, 5]
numbers_3 = [0, 3, 6]
numbers_4 = []

#Note: when working with integers, a value of 0 is "falsy"; all other integers are "truthy".

print(any(remainders_3(numbers_1))) #True
print(any(remainders_3(numbers_2))) #True
print(any(remainders_3(numbers_3))) #False
print(any(remainders_3(numbers_4))) #False



#any(collection_ => True/False if *any* of the collection's elements are truthy