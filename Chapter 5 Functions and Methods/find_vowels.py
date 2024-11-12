#Write a function find_vowels that takes a string as an argument and returns a list containing all of the vowels
# present in that string. The vowels should old appear once in the output list and should be alphabetized.
VOWELS = 'aeiou'

def find_vowels(text):
    """
        Find all unique vowels in a string and return them in alphabetical order.

        Args:
            text (str): The input string to search for vowels

        Returns:
            list[str]: A sorted list of unique vowels found in the text

        Example:
            >>> find_vowels("hello")
            ['e', 'o']
            >>> find_vowels("APPLE")
            ['a', 'e']
        """
    found_vowels = set()
    text = text.lower()
    for char in text:
        if char in VOWELS:
            found_vowels.add(char)
    return sorted(found_vowels)

print(find_vowels("hello"))
print(find_vowels("APPLE"))
print(find_vowels("rhythm"))
print(find_vowels("AeIoU"))