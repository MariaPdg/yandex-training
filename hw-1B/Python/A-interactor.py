def output(r, i, c):

    if i == 0:
        if r != 0:
            return 3
        return c
    elif i == 1:
        return c
    elif i == 4:
        if r != 0:
            return 3
        return 4
    elif i == 6:
        return 0
    elif i == 7:
        return 1
    return i


if __name__ == '__main__':

    "Output the result of the testing system"

    r = int(input())
    i = int(input())
    c = int(input())
    res = output(r, i, c)
    print(res)