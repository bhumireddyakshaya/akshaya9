def split_and_add(arr, position):
    # Split the array into two parts
    first_part = arr[:position]
    second_part = arr[position:]

    # Concatenate the parts in reverse order
    result = second_part + first_part

    return result

# Input the value of n
n = int(input("Enter the value of n: "))

# Input the numbers
print("Enter the numbers:")
numbers = []
for i in range(n):
    num = int(input())
    numbers.append(num)

# Input the position to split the array
position = int(input("Enter the position of the element to split the array: "))

# Call the function to split and add
result_array = split_and_add(numbers, position)

# Print the resultant array
print("The resultant array is:")
for num in result_array:
    print(num)
