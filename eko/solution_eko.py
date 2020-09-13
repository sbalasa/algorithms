"""
Solution code

Author: Santhosh Balasa (santhosh.kbr@yandex.com)
To run:
python solution_eko.py
"""


def solution_one():
    print("Solution One:")
    sequences = [[1, 1], [0, 0], [0, 1], [1, 1, 1], [1, 0, 1], [1, 1, 0, 0, 1]]
    res = []
    for s in sequences:
        count = 0
        for c, i in enumerate(s):
            try:
                if i == s[c + 1]:
                    count += 1
            except IndexError:
                res.append(count)
                count = 0
    [print(x) for x in res]
    print("-" * 100)
    print("\n")


def solution_two():
    print("Solution Two:")

    def generate_matrix(m, n):
        _matrix = []
        for i in range(m):
            row = []
            for j in range(n):
                row.append(i + 1)
            _matrix.append(row)
        return _matrix

    def find_paths(matrix, path, hops, points, i, j, sum_value):
        m, n = len(matrix), len(matrix[0])
        if i == m - 1 and j == n - 1:
            if sum(path + [matrix[i][j]]) == sum_value:
                # print(path + [matrix[i][j]])
                a, b = points[-1]
                if a == i:
                    hops += "R"
                else:
                    hops += "D"
                print(hops)
            return
        path.append(matrix[i][j])
        points.append((i, j))
        try:
            a, b = points[-2]
            if a == i:
                hops += "R"
            else:
                hops += "D"
        except IndexError:
            pass

        # move right
        if 0 <= i < m and 0 <= j + 1 < n:
            find_paths(matrix, path, hops, points, i, j + 1, sum_value)

        # move down excluding first column
        if 0 <= i + 1 < m and 1 <= j < n:
            find_paths(matrix, path, hops, points, i + 1, j, sum_value)

        # Clear for next iteration
        path.pop()
        points.pop()

    print("4 x 4 matrix:\n")
    matrix1 = generate_matrix(4, 4)
    print("For sum = 13:")
    find_paths(matrix1, [], "", [], 0, 0, 13)
    print("\nFor sum = 16:")
    find_paths(matrix1, [], "", [], 0, 0, 16)
    print("\nFor sum = 19:")
    find_paths(matrix1, [], "", [], 0, 0, 19)

    # print("\n9 x 9 matrix:\n")
    # matrix2 = generate_matrix(9, 9)
    # print("For sum = 65:")
    # find_paths(matrix2, [], "", [], 0, 0, 65)
    # print("\nFor sum = 72:")
    # find_paths(matrix2, [], "", [], 0, 0, 72)
    # print("\nFor sum = 90:")
    # find_paths(matrix2, [], "", [], 0, 0, 90)
    # print("\nFor sum = 110:")
    # find_paths(matrix2, [], "", [], 0, 0, 110)

    # print("9 x 10000 matrix:\n")
    # matrix3 = generate_matrix(9, 1000)
    # find_paths(matrix3, [], "", [], 0, 0, 2831)
    # print()
    # find_paths(matrix3, [], "", [], 0, 0, 4788)
    # print()
    # find_paths(matrix3, [], "", [], 0, 0, 5659)
    # print()
    # find_paths(matrix3, [], "", [], 0, 0, 6113)

    print("-" * 100)
    print("\n")


def solution_three():
    print("Solution Three:")
    input_image1 = [[0, 0, 1, 1, 1], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 1, 1, 1, 1]]

    def count_components(input_image, m, n):
        count = 0
        for i in range(0, m):
            for j in range(0, n):
                if input_image[i][j] == 1:
                    if (i == 0 or input_image[i - 1][j] == 0) and (j == 0 or input_image[i][j - 1] == 0):
                        count += 1
        return count

    print(
        f"No. of 4-Connectivity Components: {count_components(input_image1, len(input_image1), len(input_image1[0]))}"
    )
    print("-" * 100)
    print("\n")


def solution_four():
    print("Solution Four:")
    polygon = [(1, 1), (1, 5), (10, 5), (10, 1)]
    points = [(3, 3), (7, 5), (5, 6)]
    max_x, max_y = max(polygon)
    for i in points:
        print("Inside") if i[0] <= max_x and i[1] <= max_y else print("Outside")
    print("-" * 100)
    print("\n")


if __name__ == "__main__":
    solution_one()
    solution_two()
    solution_three()
    solution_four()
