def is_seen_before(arr):

    dct = {}
    for item in arr:
        if item not in dct:
            dct[item] = 0
            print('NO')
        dct[item] += 1
        if dct[item] > 1:
            print('YES')


if __name__ == '__main__':

    """Print whether the number is seen before"""

    line1 = [int(x) for x in input().split()]
    is_seen_before(line1)
