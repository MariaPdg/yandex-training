def check_gt(arr, m, target):
    return arr[m] > target


def check_ge(arr, m, target):
    return arr[m] >= target


def left_binserach(l, r, params, check):
    arr, L = params
    while l < r:
        m = l + (r - l) // 2
        if check(arr, m, L):
            r = m
        else:
            l = m + 1
    return l


def right_binserach(l, r, params, check):
    arr, R = params
    while l < r:
        m = (l + r + 1) // 2
        if not check(arr, m, R):
            l = m
        else:
            r = m - 1
    return l


if __name__ == '__main__':

    """Find indices of the left and right occurrences of t from targets"""

    n = int(input())
    arr = [int(x) for x in input().split()]
    m = int(input())
    targets = [int(x) for x in input().split()]

    for t in targets:
        left = left_binserach(0, n - 1, (arr, t), check_ge) + 1
        right = right_binserach(0, n - 1, (arr, t), check_gt) + 1
        if arr[left - 1] != t and arr[right - 1] != t:
            left = right = 0
        print(left, right)
