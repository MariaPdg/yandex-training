def is_unique(arr):

    dct = {}
    res = []
    for item in arr:
        if item not in dct:
            dct[item] = 0
        dct[item] += 1
    for item in dct:
        if dct[item] == 1:
            res.append(item)
    return res


if __name__ == '__main__':

    """Print whether the number is unique"""

    line1 = [int(x) for x in input().split()]
    res = is_unique(line1)
    print(*res)

