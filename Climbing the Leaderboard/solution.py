import os


def search(array, value, left, right):
    if right - left == 1:
        if array[left] == value:
            return left
        if array[right] == value:
            return right
        return left + 1
    mid = round((left + right) / 2)
    if array[mid] == value:
        return mid
    if array[mid] < value:
        return search(array, value, left, mid)
    if array[mid] > value:
        return search(array, value, mid, right)


# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    scores = sorted(set(scores), reverse=True)
    length = len(scores)
    _max = scores[0]
    _min = scores[-1]
    remember_dict = {}
    results = []
    for a in alice:
        if a >= _max:
            results.append(1)
            continue
        if a == _min:
            results.append(length)
            continue
        if a < _min:
            results.append(length + 1)
            continue
        if a in remember_dict:
            results.append(remember_dict[a])
        else:
            result = search(scores, a, 0, length - 1)
            results.append(result + 1)
            remember_dict[a] = result + 1
    return results


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
