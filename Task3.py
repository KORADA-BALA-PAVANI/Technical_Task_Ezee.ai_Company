def find_second_and_fourth_greatest(numbers):
    if len(numbers) < 4:
        return "Error: The list should have at least 4 numbers."
    unique_numbers = set(numbers) 
    sorted_unique_numbers = sorted(unique_numbers, reverse=True)

    if len(sorted_unique_numbers) >= 4:
        second_greatest = sorted_unique_numbers[1]
        fourth_greatest = sorted_unique_numbers[3]
        return f"The second greatest number is {second_greatest} \nThe fourth greatest number is {fourth_greatest}."
    else:
        return "Error: The list should have at least 4 unique numbers."

numbers_list = list(map(int,input().split())) 
result = find_second_and_fourth_greatest(numbers_list)
print(result)
