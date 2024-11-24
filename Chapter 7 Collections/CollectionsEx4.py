#Question: Why can we treat strings as sequences (rather than collections)?

#Answer: We can treat strings as sequences because they are ordered and therefore able to be accessed through indexing

string = 'abcdef'
print(string[1])
print(list(string))
print(set('aabbcc')) #sets aren't allowed to have duplicates, sets don't have order

