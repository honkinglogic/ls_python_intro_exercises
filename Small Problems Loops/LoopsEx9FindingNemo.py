#Loop over the elements of the fish_list list below, logging each one.
# Terminate the loop immediately after printing the string 'Nemo'.

fish_list = ['Dory', 'Marlin', 'Gill', 'Nemo', 'Bruce']
#
# for fish in fish_list:
#     print(fish)
#     if fish == 'Nemo':
#         break


#Can you achieve the same result using a while loop? What would the code look like?

i = 0
while i < len(fish_list):
    print(fish_list[i])
    if fish_list[i] == 'Nemo':
        break
    i += 1