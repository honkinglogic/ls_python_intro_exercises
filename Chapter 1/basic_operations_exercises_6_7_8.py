#6: To what value does the following expression evaluate?
'foo' == 'Foo'

#This should evaluate to false, because == is a comparison operator and the two operands are not equal because case
#matters when comparing strings

#7 What will the following code do? Why?
int('3.1415')

#It will raise a ValueError because the string value 3.1315 is not a valid integer

#8 To what value does the following expression evaluate:
'12' < '9'

#This evaluates to true because the operands are strings, not numbers. Python performs a character-by-character
# comparison from left to right when comparing strings, so the string '1' is less than the string '9'