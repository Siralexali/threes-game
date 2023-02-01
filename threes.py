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
            if mat[i][j] == 0:
                break
            elif mat[i][j] > 2 and (mat[i][j] == mat[i][j+1]):
                mat[i][j] = mat[i][j] + mat[i][j+1]
                mat[i][j+1] = 0
                break
            elif (mat[i][j] == 1 and mat[i][j+1] == 2) or (mat[i][j] == 2 and mat[i][j+1] == 1):
                mat[i][j] = mat[i][j] + mat[i][j+1]
                mat[i][j+1] = 0
                break
    return mat


def randoml(mat, k, d):
    m = 0
    tmp = {}
    key = []
    for i in range(len(mat)):
        if 0 == mat[i][-1]:
            m += 1
            key = [i]
    i = 0
    for x in key:
        tmp[i] = x
        i += 1
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
            if mat[i][j] == 0:
                break
            elif mat[i][j] > 2 and (mat[i][j] == mat[i][j-1]):
                mat[i][j] = mat[i][j] + mat[i][j-1]
                mat[i][j-1] = 0
                break
            elif (mat[i][j] == 1 and mat[i][j-1] == 2) or (mat[i][j] == 2 and mat[i][j-1] == 1):
                mat[i][j] = mat[i][j] + mat[i][j-1]
                mat[i][j-1] = 0
                break
    return mat


def randomr(mat, k, d):
    m = 0
    tmp = {}
    key = []
    for i in range(len(mat)):
        if 0 == mat[i][0]:
            m += 1
            key = [i]
    i = 0
    for x in key:
        tmp[i] = x
        i += 1
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
            if mat[j][i] == 0:
                break
            elif mat[i][j] > 2 and (mat[i][j] == mat[i+1][j]):
                mat[i][j] = mat[i][j] + mat[i+1][j]
                mat[i+1][j] = 0
                break
            elif (mat[i][j] == 1 and mat[i+1][j] == 2) or (mat[i][j] == 2 and mat[i+1][j] == 1):
                mat[i][j] = mat[i][j] + mat[i+1][j]
                mat[i+1][j] = 0
                break
    return mat


def randomu(mat, k, d):
    m = 0
    tmp = {}
    key = []
    for i in range(len(mat)):
        if 0 == mat[-1][i]:
            m += 1
            key = [i]
    i = 0
    for x in key:
        tmp[i] = x
        i += 1
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
            if mat[j][i] == 0:
                break
            elif mat[i][j] > 2 and (mat[i][j] == mat[i-1][j]):
                mat[i][j] = mat[i][j] + mat[i-1][j]
                mat[i-1][j] = 0
                break
            elif (mat[i][j] == 1 and mat[i-1][j] == 2) or (mat[i][j] == 2 and mat[i-1][j] == 1):
                mat[i][j] = mat[i][j] + mat[i-1][j]
                mat[i-1][j] = 0
                break
    return mat


def randomd(mat, k, d):
    m = 0
    tmp = {}
    key = []
    for i in range(len(mat)):
        if 0 == mat[0][i]:
            m += 1
            key = [i]
    i = 0
    for x in key:
        tmp[i] = x
        i += 1
    mat[0][tmp[k % m]] = d
    return mat


for i in side:
    if i == 'R':
        mat1 = [i[:] for i in mat]
        if right(mat) != mat1:
            kd = input().split()
            k = int(kd[0])
            d = int(kd[1])
            randomr(mat, k, d)
    elif i == 'L':
        mat1 = [i[:] for i in mat]
        if left(mat) != mat1:
            kd = input().split()
            k = int(kd[0])
            d = int(kd[1])
            randomr(mat, k, d)
    elif i == 'U':
        mat1 = [i[:] for i in mat]
        if left(mat) != mat1:
            kd = input().split()
            k = int(kd[0])
            d = int(kd[1])
            randomr(mat, k, d)
    elif i == 'D':
        mat1 = [i[:] for i in mat]
        if left(mat) != mat1:
            kd = input().split()
            k = int(kd[0])
            d = int(kd[1])
            randomr(mat, k, d)

for i in range(len(mat)):
    for j in range(len(mat)):
        print(mat[i][j], end='	')
    print()


score = 0
for i in range(len(mat)):
    for j in range(len(mat)):
        if mat[i][j] > 2:
            div = mat[i][j] // 3
            power = 0
            while 2 ** power != div:
                power += 1
            score += 3 ** (power + 1)

mat1 = [i[:] for i in mat]
if (mat1 == right(mat)) and (mat1 == (up(mat)) and ((mat1) == down(mat)) and (mat1 == left(mat))):
    print('The final score is ' + str(score) + '.')
else:
    print('The partial score is ' + str(score) + '.')
