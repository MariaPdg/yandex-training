from collections import Counter


def count_cats(arr, size):

    prefix = [0] * (size + 2)
    arr_cnt = Counter(arr)
    for i in range(1, size+2):
        prefix[i] = prefix[i-1] + arr_cnt[i-1] if i-1 in arr_cnt else prefix[i-1]
    print(prefix)
    return prefix


def answer(arr, events, max_p, min_p):

    size = max_p - min_p + 1
    prefix = count_cats(arr, size)
    return [prefix[e[1]+1] - prefix[e[0]] for e in events]


if __name__ == '__main__':

    """The problem is about cats, reformulation: 
    How many points (arr) does each segment (events[i]) cover?"""

    n, m = map(int, input().split())
    events = []
    arr = [int(x) for x in input().split()]
    max_point = 0
    min_point = 10e9
    for i in range(m):
        l, r = map(int, input().split())
        events.append((l, r))
        max_point = max(max_point, r)
        min_point = min(min_point, l)
    res = answer(arr, events, max_point, min_point)
    print(*res)

