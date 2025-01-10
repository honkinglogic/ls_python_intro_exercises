#Without running the following code, determine what each print statement should print.

cats = ('Cocoa', 'Cheddar',
        'Pudding', 'Butterscotch')
print('Butterscotch' in cats)       # True
print('Butter' in cats)             # False   #in won't search substrings
print('Butter' in cats[3])          # True   - now it's looking at the substring
print('cheddar' in cats)            # False   - case sensitive when comparing strings 'a' != 'A'

