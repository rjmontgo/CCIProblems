# 1.8
# Write a function that will find the 0 values in a matrix and convert the row
# and column of the index to 0

def zeroMatrix(mat):
    if len(mat) is 0 or len(mat[0]) is 0:
        return mat

    # These are used to improve best case. If a matrix is all 0s or all non-0s
    # then these flags will let us return out of the function before the final
    # two loops.

    nullFirstCol = False
    nullFirstRow = False
    for i, row in enumerate(mat):
        for j, val in enumerate(row):
            if row[j] is 0:
                mat[0][j] = 0
                mat[i][0] = 0
                if j is 0:
                    nullFirstCol = True
                if i is 0:
                    nullFirstRow = True

    for i, row in enumerate(mat):
        if row[0] is 0 and i is not 0:
            for j, val in enumerate(row):
                row[j] = 0

    for j, val in enumerate(mat[0]):
        if val is 0 and j is not 0:
            for i, row in enumerate(mat):
                row[j] = 0

    # Discovered mid-problem that with this solution you cannot
    # zero out the first row and col until the end

    if (nullFirstCol):
        for i, row in enumerate(mat):
            row[0] = 0
    if (nullFirstRow):
        for j, val in enumerate(mat[0]):
            mat[0][j] = 0
    return mat
