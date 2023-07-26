# Input_sentence = “Hello, World!"
# Output after reverse

def reverse_sentence(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

# Input sentence
input_sentence = "Hello, World! Welcome to Python programming."

# Call the function to reverse the sentence
output = reverse_sentence(input_sentence)

# Print the output
print("Output after reverse:", output)
