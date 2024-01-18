def process_string(input_string):
    cleaned_chars = [char if char.isalpha() or char.isspace() else ' ' for char in input_string]
    cleaned_string = ''.join(cleaned_chars)
    return cleaned_string

input_string = input()
result = process_string(input_string)
print("Original String :", input_string)
print("String after replacement :", result)
