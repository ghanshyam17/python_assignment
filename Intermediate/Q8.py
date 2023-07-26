# Input: string = "Hello, World!"
# Output: Number of vowels: 3

def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = 0

    for char in input_string:
        if char in vowels:
            count += 1

    return count

string = "Hello, World!"
vowel_count = count_vowels(string)
print("Number of vowels:", vowel_count)
