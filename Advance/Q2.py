# program to count the lines in a file “demo.txt”

def count_lines_in_file(file_path):
    with open(file_path, 'r') as file:
        line_count = len(file.readlines())
    return line_count

file_path = 'demo.txt'
line_count = count_lines_in_file(file_path)
print("Number of lines in the file:", line_count)
