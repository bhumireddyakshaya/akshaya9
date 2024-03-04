def find_union_intersection(arr1, arr2):
    # Convert arrays to sets for easier manipulation
    set1 = set(arr1)
    set2 = set(arr2)

    # Intersection of the two sets
    intersection = set1.intersection(set2)

    # Union of the two sets
    union = set1.union(set2)

    return sorted(list(intersection)), sorted(list(union))

# Function to input elements of an array
def input_array():
    n = int(input("Enter the number of elements: "))
    arr = []
    for i in range(n):
        element = int(input("Enter element {}: ".format(i + 1)))
        arr.append(element)
    return arr

# Main program
print("Enter the elements of Array 1:")
array1 = input_array()
print("\nElements of Array 1:", array1)
print("Sorted elements of Array 1:", sorted(array1))

print("\nEnter the elements of Array 2:")
array2 = input_array()
print("\nElements of Array 2:", array2)
print("Sorted elements of Array 2:", sorted(array2))

intersection, union = find_union_intersection(array1, array2)

print("\nIntersection is:", intersection)
print("Union is:", union)
