def find_missing_numbers(arr):
    # Define the range of numbers based on the minimum and maximum values in the array
    min_num = min(arr)
    max_num = max(arr)
    
    # Initialize a list to store missing numbers
    missing_numbers = []
    
    # Iterate over the range of numbers
    for num in range(min_num, max_num + 1):
        # If the number is not in the array, it's missing
        if num not in arr:
            missing_numbers.append(num)
    
    return missing_numbers

# Example usage
arr = [1, 2, 4, 6, 7, 10]
print("Missing numbers:", find_missing_numbers(arr))
