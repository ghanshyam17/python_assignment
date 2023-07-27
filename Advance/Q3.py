def JtoI(file_path):
    corrected_content = ""
    with open(file_path, 'r') as file:
        content = file.read()
        corrected_content = content.replace("J", "I")
        corrected_content = corrected_content.replace("j", "i")

    return corrected_content

file_path = 'words.txt'
corrected_content = JtoI(file_path)
print(corrected_content)
