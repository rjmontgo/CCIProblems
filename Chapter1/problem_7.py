from math import floor

def rotate(matrix):
    offset = 0
    for j in range(floor(len(matrix) / 2)):
        for i in range(len(matrix) - 1 - offset*2):
            temp = matrix[0 + offset][i + offset]

            # copy left to top
            matrix[0 + offset][i + offset] = matrix[len(matrix) - i - 1 - offset][0 + offset]
            # copy bottom to left
            matrix[len(matrix) - i - 1 - offset][0 + offset] = \
                matrix[len(matrix) - 1 - offset][len(matrix) - i - 1 - offset]
            # copy right to bottom
            matrix[len(matrix) - 1 - offset][len(matrix) - i - 1 - offset] = \
                matrix[i + offset][len(matrix) - 1 - offset]
            # copy top to right
            matrix[i + offset][len(matrix) - 1 - offset] = temp

        offset += 1
    return matrix

# [1, 2] -> [3, 1]
# [3, 4]    [4, 2]

# [4, 3]
# [2, 1]
