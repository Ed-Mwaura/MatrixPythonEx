def matrix_init():
    matrix_dimensions = input()

    int_coordinates = [int(x) for x in matrix_dimensions.split(" ")]

    rows = []
    rows_list = []
    for x in range(int_coordinates[0]):
        row_data = input()
        rows_list.append(row_data.split())
        int_coordinates[0] += 1

    for y in rows_list:
        rows_int = [int(x) for x in y]
        rows.append(rows_int)

    return rows


mat1 = matrix_init()

mat2 = matrix_init()

if len(mat1) != len(mat2):
    print("ERROR")
else:
    for i, j in zip(mat1, mat2):
        if len(i) != len(j):
            print("ERROR")
        else:
            result = [a + b for a, b in zip(i, j)]
            for i in result:
                print(i, end=" ")
            print()
