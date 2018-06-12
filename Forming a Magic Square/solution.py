import os
from itertools import permutations


def validate(s):
    constant = 15
    if sum(s[0:3]) != constant or sum(s[3:6]) != constant or sum(s[6:9]) != constant \
            or s[0] + s[3] + s[6] != constant or s[1] + s[4] + s[7] != constant or s[2] + s[5] + s[8] != constant \
            or s[0] + s[4] + s[8] != constant or s[2] + s[4] + s[6] != constant:
        return False
    return True


def generate():
    possibles = permutations(range(1, 10))
    results = []
    for possible in possibles:
        if validate(possible):
            results.append([possible[0:3], possible[3:6], possible[6:9]])
    return results


pre = generate()


def formingMagicSquare(s):
    totals = []
    for p in pre:
        total = 0
        for p_row, s_row in zip(p, s):
            for i, j in zip(p_row, s_row):
                if not i == j:
                    total += max([i, j]) - min([i, j])
        totals.append(total)
    return min(totals)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
