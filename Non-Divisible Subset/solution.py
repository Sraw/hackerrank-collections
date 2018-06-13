import os

global_dict = {}


def compute(S, k):
    d = {x: [] for x in range(k)}

    for item in S:
        d[item % k].append(item)

    count = 0

    if len(d[0]) > 0:
        count = 1

    S = {(x, k - x) for x in range(1, k//2+1)}

    for i, j in S:
        if i != j:
            count += max(len(d[i]), len(d[j]))
        else:
            if len(d[i]) > 0:
                count += 1
    return count


# Complete the nonDivisibleSubset function below.
def nonDivisibleSubset(k, S):
    return compute(S, k)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    S = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, S)

    fptr.write(str(result) + '\n')

    fptr.close()
