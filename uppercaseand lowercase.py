def count_characters():
    uppercase_count = 0
    lowercase_count = 0
    number_count = 0
    print("Enter * to exit")
    while True:
        char = input("enter any character")
        if char == '*':
            break
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
        elif char.isdigit():
            number_count += 1
    print("\nResults:")
    print("Total count of lower case:", uppercase_count)
    print("Total count of upper case: ", lowercase_count)
    print("Total count of Numbers:", number_count)
count_characters()
