def str_add(a, b):
    length = max(len(a), len(b))
    a = a.rjust(length, "0")
    b = b.rjust(length, "0")
    result = []
    temp = 0
    for i in range(length - 1, -1, -1):
        temp_result = int(a[i]) + int(b[i])
        up = False
        if temp_result + temp >= 10:
            up = True
        temp_result = (temp_result + temp) % 10
        result.append(str(temp_result))
        if up:
            temp = 1
        else:
            temp = 0
    if temp == 1:
        result.append(str(temp))
    return "".join(result[::-1])


def str_mul(a, b):
    b = int(b)
    result = "0"
    for i in range(b):
        result = str_add(result, a)
    return result


# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    result = "1"
    for i in range(1, n + 1):
        result = str_mul(result, str(i))
    print(result)


if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)
