#Without running the following code, determine what it will print:

def multiples_of_three():
    divisor = 1

    for dividend in range(3, 31, 3):
        print(f'{dividend} / {divisor} = 3')
        divisor += 1

multiples_of_three()

# ( ) REQUIRED to INVOKE any function! Otherwise nothing will print!



# 3, 6, 9, 12, 15, 18, 21, 24, 27, 30
#
# 3 / 1 = 3
# 6 / 2 = 3