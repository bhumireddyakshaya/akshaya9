def draw_diamond(rows):
    for i in range(1, rows + 1):
        # Print spaces before the stars
        print(" " * (rows - i), end="")
        # Print stars
        print("* " * i)

    for i in range(rows - 1, 0, -1):
        # Print spaces before the stars
        print(" " * (rows - i), end="")
        # Print stars
        print("* " * i)


rows = int(input("Enter the number of rows for the diamond: "))
draw_diamond(rows)
