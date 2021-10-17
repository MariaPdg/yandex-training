def left_binsearch(l, r, params):
    arr, L = params
    while l < r:
        m = l + (r - l) // 2
        if arr[m] >= L:
            r = m
        else:
            l = m + 1
    return l


def right_binsearch(l, r, params):
    arr, R = params
    while l < r:
        m = (l + r + 1) // 2
        if arr[m] <= R:
            l = m
        else:
            r = m - 1
    return l


if __name__ == '__main__':

    """How many numbers in a range [L, R]?"""

    n = int(input())
    arr = [int(x) for x in input().split()]
    arr.sort()
    k = int(input())
    ans = [0] * k

    for i in range(k):
        L, R = map(int, input().split())
        left = left_binsearch(0, len(arr)-1, (arr, L))
        right = right_binsearch(0, len(arr)-1, (arr, R))
        if arr[left] >= L and arr[right] <= R:
            ans[i] = right - left + 1
    print(*ans)