def cut_trees_per_day(a, k, b, m, d):
    t1 = a
    t2 = b
    if not d % k:
        t1 = 0
    if not d % m:
        t2 = 0

    return t1 + t2


if __name__ == '__main__':
    a, k, b, m, x = map(int, input().split())
    cut_trees = 0
    days = 1
    while cut_trees < x:
        cut_trees += cut_trees_per_day(a, k, b, m, days)
        days += 1
    print(days-1)