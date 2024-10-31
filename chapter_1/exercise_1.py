"""
'True' string
False boolean
(1, 2, 3) tuple
1.5 float
[1, 2, 3] list
2 integer
range(5) range
{1, 2, 3} set
None  NoneType
{'foo': 'bar'} Dictionary 
"""'True'

values = ['True', False, (1, 2, 3), 1.5, [1, 2, 3], 2, range(5), {1, 2, 3} , None,  {'foo': 'bar'}]

for value in values:
    print(f"Value: {value} - type: {type(value)}")
