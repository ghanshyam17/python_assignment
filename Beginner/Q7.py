# check if a string is an anagram of another string.
# string1 = "listen", string2 = "silent"

def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

# Get input from the user
string1 = input("Enter the first string: ").lower()
string2 = input("Enter the second string: ").lower()

# Check if the strings are anagrams using the is_anagram function
if is_anagram(string1, string2):
    print("True")
else:
    print("False")
