max_num = 0
count = 0

number = int(input())

while number != 0:
    if number > max_num:  # Changed max_number to max_num
        max_num = number
        count = 1
    elif number == max_num:  # Changed max_number to max_num
        count += 1

    number = int(input())  # Fixed typo in number

print(count)