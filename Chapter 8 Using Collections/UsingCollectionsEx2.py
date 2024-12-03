#Use slicing to write Python code to print a 6-character substring of 'Launch School' that begins with the first c.

my_string = 'Launch School'
my_string2 = "My cat is the best"
# print(my_string[4:10])

start = my_string2.find('c')
#print(start)
print(my_string2[start:start + 6])