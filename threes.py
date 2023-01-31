size = int(input())
mat = []
for i in range(size):
    s = input().split()
    for j in range(size):
        s[j] = int(s[j])
    mat += [s]

side = input()


def left(mat):
    tedad = len(mat)
    for i in range(tedad):
        for j in range(tedad-1):
            if mat[i][j] == 0:
                (mat[i][j], mat[i][j+1]) = (mat[i][j+1], mat[i][j])
    for i in range(tedad):
        for j in range(tedad-1):
            if mat[i][j] > 2 and (mat[i][j] == mat[i][j+1]):
                mat[i][j] = mat[i][j] + mat[i][j+1]
                mat[i][j+1] = 0
                break
            elif (mat[i][j] == 1 and mat[i][j+1] == 2) or (mat[i][j] == 2 and mat[i][j+1] == 1):
                mat[i][j] = mat[i][j] + mat[i][j+1]
                mat[i][j+1] = 0
                break
    return mat


def randoml(mat):
    m = 0
    tmp = {}
    key = []
    for i in range(len(mat)):
        if 0 == mat[i][-1]:
            m += 1
            key = [i]
    for i in range(m):
        tmp[i] = key[i]
    kd = input().split()
    k = int(kd[0])
    d = int(kd[1])
    mat[tmp[k % m]][-1] = d
    return mat


def right(mat):
    tedad = len(mat)
    for i in range(tedad):
        for j in range(-1, tedad, -1):
            if mat[i][j] == 0:
                (mat[i][j], mat[i][j-1]) = (mat[i][j-1], mat[i][j])
    for i in range(tedad):
        for j in range(-1, tedad, -1):
            if mat[i][j] > 2 and (mat[i][j] == mat[i][j-1]):
                mat[i][j] = mat[i][j] + mat[i][j-1]
                mat[i][j-1] = 0
                break
            elif (mat[i][j] == 1 and mat[i][j-1] == 2) or (mat[i][j] == 2 and mat[i][j-1] == 1):
                mat[i][j] = mat[i][j] + mat[i][j-1]
                mat[i][j-1] = 0
                break
    return mat


def randomr(mat):
    m = 0
    tmp = {}
    key = []
    for i in range(len(mat)):
        if 0 == mat[i][0]:
            m += 1
            key = [i]
    for i in range(m):
        tmp[i] = key[i]
    kd = input().split()
    k = int(kd[0])
    d = int(kd[1])
    mat[tmp[k % m]][0] = d
    return mat


def up(mat):
    tedad = len(mat)
    for j in range(tedad):
        for i in range(tedad-1):
            if mat[i][j] == 0:
                (mat[i][j], mat[i+1][j]) = (mat[i+1][j], mat[i][j])
    for j in range(tedad):
        for i in range(tedad-1):
            if mat[i][j] > 2 and (mat[i][j] == mat[i+1][j]):
                mat[i][j] = mat[i][j] + mat[i+1][j]
                mat[i+1][j] = 0
                break
            elif (mat[i][j] == 1 and mat[i+1][j] == 2) or (mat[i][j] == 2 and mat[i+1][j] == 1):
                mat[i][j] = mat[i][j] + mat[i+1][j]
                mat[i+1][j] = 0
                break
    return mat


def randomu(mat):
    m = 0
    tmp = {}
    key = []
    for i in range(len(mat)):
        if 0 == mat[-1][i]:
            m += 1
            key = [i]
    for i in range(m):
        tmp[i] = key[i]
    kd = input().split()
    k = int(kd[0])
    d = int(kd[1])
    mat[-1][tmp[k % m]] = d
    return mat


def down(mat):
    tedad = len(mat)
    for j in range(tedad):
        for i in range(-1, tedad, -1):
            if mat[i][j] == 0:
                (mat[i][j], mat[i-1][j]) = (mat[i-1][j], mat[i][j])
    for j in range(tedad):
        for i in range(-1, tedad, -1):
            if mat[i][j] > 2 and (mat[i][j] == mat[i-1][j]):
                mat[i][j] = mat[i][j] + mat[i-1][j]
                mat[i-1][j] = 0
                break
            elif (mat[i][j] == 1 and mat[i-1][j] == 2) or (mat[i][j] == 2 and mat[i-1][j] == 1):
                mat[i][j] = mat[i][j] + mat[i-1][j]
                mat[i-1][j] = 0
                break
    return mat


def randomd(mat):
    m = 0
    tmp = {}
    key = []
    for i in range(len(mat)):
        if 0 == mat[0][i]:
            m += 1
            key = [i]
    for i in range(m):
        tmp[i] = key[i]
    kd = input().split()
    k = int(kd[0])
    d = int(kd[1])
    mat[0][tmp[k % m]] = d
    return mat
