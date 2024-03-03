def generate_pascals_triangle(rows):
    triangle = []
    for i in range(rows):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle

def print_pascals_triangle(triangle):
    for row in triangle:
        print(" ".join(map(str, row)).center(len(triangle[-1]) * 3))

rows = 6  # Number of rows in Pascal's Triangle
pascals_triangle = generate_pascals_triangle(rows)
print_pascals_triangle(pascals_triangle)
