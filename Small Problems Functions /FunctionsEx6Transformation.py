#Use Python's string methods on the string 'Captain Ruby' to create a string with the value 'Captain Python'.

def transformation(str1, str2):
    new_str = str1.replace(str1, str2)
    return new_str

print(transformation("Captain Ruby", "Captain Python"))