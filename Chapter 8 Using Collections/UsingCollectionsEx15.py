pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',     #deleted
    'Bird': 'Tweet',
    #'Snake': 'Ssss',
}

keys = pets.keys()
del pets['Dog']
pets['Snake'] = 'Sssss'
print(keys)     # 'Cat', 'Bird', 'Snake'

#Without running the following code, what values will be printed by line 10?

#Dictionary view objects are live collections