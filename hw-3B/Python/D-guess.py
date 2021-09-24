def difference(a1, a2):
    return set(a1) - set(a2)


def help(a, ans_b, ans_a):
    """
    :param a: range of numbers
    :param ans_b: answers of Beatrisa
    :param ans_a:  answers of August
    :return: possible numbers
    """

    res = ans_b[0]
    dct = {}
    if ans_a[0] == 'YES':
        for item in res:
            dct[item] = 1
    else:
        for item in list(difference(range(1, a + 1), res)):
            dct[item] = 1
    res = list(dct.keys())

    for i in range(1, len(ans_b)):
        if ans_a[i] == 'NO':
            for item in ans_b[i]:
                if item in dct:
                    dct[item] = 0
        else:
            for item in difference(res, ans_b[i]):
                dct[item] = 0
    res = []
    for k, v in dct.items():
        if v == 1:
            res.append(k)
    return res


if __name__ == '__main__':

    """Beatrisa tries to guess the secret number of August. 
       Compute the possible numbers, which can be secret."""

    n = int(input())
    res = []
    ans_A, ans_B = [], []
    while True:
        ans = input()
        if ans != "HELP":
            ans_B.append([int(x) for x in ans.split()])
        else:
            break
        ans_A.append(input())
    res = help(n, ans_B, ans_A)
    print(*sorted(res))
