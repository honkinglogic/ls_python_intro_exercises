#Write code that capitalizes the words in the string 'launch school tech & talk', so that you get the string
# 'Launch School Tech & Talk'.

def capitalize_words(string):
    words = string.split(' ')
    capitalize_words = []

    for word in words:
        capitalize_words.append(word.capitalize())

    return ' '.join(capitalize_words)

string = 'launch school tech & talk'
result = capitalize_words(string)
print(result)

# def capitalize(s):
#     words = s.title()
#     print(words)

# capitalize("launch school & tech talk")