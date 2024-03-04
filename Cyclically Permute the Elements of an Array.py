def cyclically_permute(arr):
    # Check if the array is empty or has only one element
    if len(arr) <= 1:
        return arr
    
    # Store the last element to be moved to the first position
    last_element = arr[-1]
    
    # Shift all elements to the right by one position
    for i in range(len(arr) - 1, 0, -1):
        arr[i] = arr[i - 1]
    
    # Move the last element to the first position
    arr[0] = last_element
    
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
print("Original array:", arr)
print("Cyclically permuted array:", cyclically_permute(arr))
