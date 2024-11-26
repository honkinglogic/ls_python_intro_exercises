#How would you print all the numbers in the following range?

print(list(range(3, 17, 4)))  #[3, 7, 11, 15]

#Ranges are lazy sequences, so you must iterate over the range, or convert the range to a non-lazy sequence:
# a list or a tuple