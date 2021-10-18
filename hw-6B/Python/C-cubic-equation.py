def equation(params, x):
    a, b, c, d = params
    return a * x**3 + b * x**2 + c * x + d


def check_pos(m, params):
    return equation(params, m) > 0


def check_neg(m, params):
    return equation(params, m) < 0


def left_binsearch(check, l, r, params, eps=10e-6):
    while l + eps < r:
        m = (r + l) / 2.0
        if check(m, params):
            r = m
        else:
            l = m
    return l


if __name__ == '__main__':

    """Solve cubic equation"""

    eps = 2e-7
    coef = [int(x) for x in input().split()]
    if coef[0] > 0:
        ans = left_binsearch(check_pos, -1001, 1001, coef, eps)
    else:
        ans = left_binsearch(check_neg, -1001, 1001, coef, eps)
    print(ans)