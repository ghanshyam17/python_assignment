# Read the doc.txt file using Python File handling concept and return only the even length string
# from the file. Consider the content of doc.txt as given below:
# Hello I am a file
# Where you need to return the data string which is of even length.Make sure you return the content in The same link as it is present.

def get_even_length_strings(file_path):
    even_length_strings = []
    with open(file_path, 'r') as file:
        content = file.read().split()
        for word in content:
            if len(word) % 2 == 0:
                even_length_strings.append(word)
    return ' '.join(even_length_strings)

file_path = 'doc.txt'
even_length_content = get_even_length_strings(file_path)
print(even_length_content)
