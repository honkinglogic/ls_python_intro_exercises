#Without running the following code, identify the numbers that are included in each of the following ranges:


def print_range(my_range):
    print(list(my_range))

print(list(range(7)))                  # [1,2,3,4,5,6]
print(list(range(1, 6)) )                # [1, 2, 3, 4, 5]
print(list(range(3, 15, 4)))             # [3, 7, 11]
print(list(range(3, 8, -1)))             # error
print(list(range(8, 3, -1)))             # [8, 7, 6, 5, 4]


#NOTE: Ranges never include the "stop" value

#1 arguments (0, stop)
#2 arguments (start, stop)
#3 arguments (start, stop, step)



