def string_conversion(input_string):
    if len(input_string) % 2 == 1:
        midpoint = len(input_string) // 2
        converted_string = input_string[:midpoint].upper() + input_string[midpoint:].lower()
        return converted_string
    else:
        return input_string

input_string = input()
result = string_conversion(input_string)
print("Original String : ",input_string)
print("String after conversion : ",result)
