#Write code that checks whether the string char_sequence contains the character x.

char_sequence = 'TXkgaG92ZXJjcmFmdCBpcyBmdWxsIG9mIGVlbHMu'
char = 'x'

if char in char_sequence:
    print(f'{char} is in sequence')
else:
    print(f'{char} is not in sequence')

#SIMPLER WAY:

print('x' in char_sequence)