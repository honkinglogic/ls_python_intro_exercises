#Write Python code to print the seventh number of range(0, 25, 3)

my_range1 = list(range(0, 25, 3))
print(my_range1[6])

my_range = range(0, 25, 3) # 0, 3, 6, 9, 12, 15, 18, 21, 24)
print(my_range[6])



#5. Which of the following values can't b used as a key in a dict object, and why>
'cat'
(3, 1, 4, 1, 5, 9, 2)
['a', 'b']
{'a': 1, 'b': 2}
range(5)
{1, 4, 9, 16, 25}
3
0.0
frozenset({1, 4, 9, 16, 25})

# anything that is mutable cannot be used as keys
['a', 'b']
{'a': 1, 'b': 2}