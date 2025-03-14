#Write a function that counts the number of occurrences of a substring in a string.

# def count_substrings(string, substring):
#     count = 0
#     i = 0
#
#     while i <= len(string) - len(substring):
#         if string[i:i + len(substring)] == substring:
#             count += 1
#         i += 1
#
#     return count

# def count_substrings(string, substring):
#     return string.count(substring)

def count_substrings(string, substring):
    count = 0
    for i in range(len(string) - len(substring) + 1):
        if string[i: i + len(substring)] == substring:
            count += 1
    return count

print(count_substrings("lemon lemon lemon", "lemon")) # 3
print(count_substrings("laLAlaLA", "la")) # 2
print(count_substrings("launch", "uno")) # 0


