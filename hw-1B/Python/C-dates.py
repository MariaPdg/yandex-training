def check_date(x, y):

    """ Tricky case: e.g. 3 3 2056 is also correct"""

    if x <= 12 and y <= 12:
        if x != y:
            return 0
    return 1


if __name__ == '__main__':

    """ Check whether the date is uniquely determined """

    x, y, z = map(int, input().split())
    res = check_date(x, y)
    print(res)