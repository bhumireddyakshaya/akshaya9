def print_non_repeated_elements(arr):
    count_dict = {}
    
    for num in arr:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    print("Non-repeated elements:")
    for num, count in count_dict.items():
        if count == 1:
            print(num)

arr = [1, 2, 3, 4, 5, 2, 3, 6, 7, 8, 7, 8]
print_non_repeated_elements(arr)
