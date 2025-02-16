#Write a loop that prints the value of the greeting variable three times.

i = 0
while i < 3:
    greeting = 'Aloha!'
    print(greeting)
    i += 1
#no need to redefine the greeting variable inside the loop each time

greeting = 'Aloha'
for _ in range(3):
    print(greeting)

#best choice


greeting = 'Aloha'
count = 1

while count <= 3:
    print(greeting)
    count += 1