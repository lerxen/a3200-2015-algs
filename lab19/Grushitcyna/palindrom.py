def find_palindrom(s):
    j = len(s)
    matrix = [[0 for k in xrange(j)] for i in xrange(j)]
    matrix2 = [[0 for k in xrange(j)] for i in xrange(j)]
    for m in xrange(j):
        matrix[m][m] = 1
    for l in xrange(1, j + 1):
        for m in xrange(j - l):
            if s[m] == s[m + l]:
                matrix[m + l][m] = matrix[m + l - 1][m + 1] + 2
                matrix2[m + l][m] = (m + l - 1, m + 1)
            else:
                if matrix[m + l - 1][m] > matrix[m + l][m + 1]:
                    matrix[m + l][m] = matrix[m + l - 1][m]
                    matrix2[m + l][m] = (m + l - 1, m)
                else:
                    matrix[m + l][m] = matrix[m + l][m + 1]
                    matrix2[m + l][m] = (m + l, m + 1)

    return matrix[j - 1][0], matrix2


def max_polindrom(matrix, matrix2, s):
    result = ''
    j = len(s)
    i = 0
    while():
        a, b = matrix2[j - 1][0]
        if matrix[j - 1][0] != matrix[a][b]:
            result += s[i]
        i = a
        j = b


a, b = find_palindrom('abaccba')
print(a)
print(b)
