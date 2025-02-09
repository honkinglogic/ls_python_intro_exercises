#What does the following function do? Be sure to identify the output value.

def do_something(dictionary):
    return sorted(dictionary.keys())[1].upper()
    # return sorted(['Karl', 'Clare', 'Karis'...])[1].upper()
    # return ['Antonina, 'Chris', 'Clare',...].[1]upper
    # return 'Chris'.upper()
    # return 'CHRIS'
my_dict = {
    'Karl':     108,
    'Clare':    175,
    'Karis':    140,
    'Trevor':   180,
    'Antonina': 132,
    'Chris':    101,
}

print(do_something(my_dict))