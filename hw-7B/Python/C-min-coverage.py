def min_cover(events, m):

    events.sort()
    res = []
    curr_right = 0
    next_right = 0
    curr_best = (0, 0)
    for e in events:
        if e[0] > curr_right:
            res.append(curr_best)
            curr_right = next_right
            if curr_right >= m:
                break
        if e[0] <= curr_right and e[1] > next_right:
            next_right = e[1]
            curr_best = e
    if curr_right < m:
        curr_right = next_right
        res.append(curr_best)
    if curr_right < m:
        print('No solution')
    else:
        print(len(res))
        for e in res:
            print(*e)

    return 0


if __name__ == '__main__':

    """Define the minimum coverage of a segment [0, m]"""

    events = []
    m = int(input())
    while True:
        a, b = map(int, input().split())
        if b > 0 and a < m:
            events.append((a, b))
        if a == b == 0:
            break
    res = min_cover(events, m)

