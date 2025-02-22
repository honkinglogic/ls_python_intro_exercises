#Write a function that extracts the language code from a locale. A locale is a combination of a language code, a region,
#and usually also a character set, e.g en_US.UTF-8.
from os.path import split


# def extract_language(locale):
#     return locale.split('_')[0]
#
#
# print(extract_language('en_US.UTF-8'))  # en
# print(extract_language('en_GB.UTF-8'))  # en
# print(extract_language('ko_KR.UTF-16'))  # ko


#Part2: Similar to the previous exercise, write a function that extracts the region code from a locale. For example:

def extract_region(locale):
    return locale.split('.')[0].split('_')[1]

print(extract_region('en_US.UTF-8'))    # US
print(extract_region('en_GB.UTF-8'))    # GB
print(extract_region('ko_KR.UTF-16'))   # KR