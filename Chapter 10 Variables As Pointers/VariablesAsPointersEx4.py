#Without running this code, what will it print? Why?

dict1 = {
    'a': [1, 2, 3],
    'b': (4, 5, 6),
}

dict2 = dict(dict1)
dict1['a'][1] = 42
print(dict2['a'])

#dict(dict1) creates a new dict object, when the list within dict1 is altered in dict1, it will be shown by the other;
#because they are referencing the same list #index reassignment is mutating action - it mutates the list

#