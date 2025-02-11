#In the following code snippet, find all violations of the PEP8 style guide. Rewrite it so that it conforms with the guide.

#wrong code:
iceCreamDensity=10

while iceCreamDensity>0 :
    print('Drip...')
    iceCreamDensity-=1

print('The ice cream melted.')


#Corrected version:
ice_cream_density = 10

while ice_cream_density > 0:
    print('Drip...')
    ice_cream_density -= 1

print('The ice cream melted.')

# Variable name should be snake_case not camelCase!
# No space before the colon in the while loop
# Add a space on both sides of the math operators