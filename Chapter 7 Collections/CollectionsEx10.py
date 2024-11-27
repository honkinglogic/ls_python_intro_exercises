
#Bob expects the following code to print the names in alphabetical order. Without running the code, can you say whether
# it will? Explain your answer.

names = { 'Chris', 'Clare', 'Karis', 'Karl',
          'Max', 'Nick', 'Victor' }
print(names)


#Sets are unordered collections, so no. We will get a different order every time.

print(sorted(names))  #you can sort it with sorted, but it changes it to a list