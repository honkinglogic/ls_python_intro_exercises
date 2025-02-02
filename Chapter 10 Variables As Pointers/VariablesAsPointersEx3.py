#Without running this code, what will it print? Why?
dict1 = {
    "Hitchhiker's Guide to the Galaxy": 42,
    'Monty Python': 'The Life of Brian',
    'Airplane!': "Don't call me Shirley!",
}

dict2 = dict(dict1)
dict2['Monty Python'] = 'Holy Grail'
print(dict1['Monty Python'])

#the constructor function dict(dict1) creates a new dict that has the same key/value pairs as dict1, but is not the same
# object as dict1. When we change the value in dict1, we don't see a corresponding change in dict1.

#This shows that 2 identical objects are not necessarily the same object. 