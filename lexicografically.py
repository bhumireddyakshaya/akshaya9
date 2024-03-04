def count_sorted_vowel_strings(n):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0

    # Helper function to generate strings recursively
    def generate_string(current_string, index):
        nonlocal count
        if index == n:
            count += 1
            return

        for vowel in vowels:
            if not current_string or vowel >= current_string[-1]:
                generate_string(current_string + vowel, index + 1)

    generate_string('', 0)
    return count

# Test
print(count_sorted_vowel_strings(1))  # Output: 5
