from math import pi


def intersection_area(events, n, rmax, rmin):

    events.sort()
    arrived = 0
    used = set()
    for event in events:
        if event[1] < 0:
            arrived += 1
            used.add(-event[1])
        elif event[1] in used:
            arrived -= 1
    ans = 0
    for i in range(len(events)):
        event = events[i]
        if event[1] < 0:
            arrived += 1
        else:
            arrived -= 1
        if arrived == n:
            last = len(events) - 1
            if i < last:
                ans += (events[i+1][0] - events[i][0]) * (rmax ** 2 - rmin ** 2) / 2
            else:
                ans += (events[0][0] - events[last][0] + 2 * pi) * (rmax ** 2 - rmin ** 2) / 2
    return ans


if __name__ == '__main__':

    """Find intersection area of polar squares"""

    with open('input.txt', 'r') as file:
        lines = file.readlines()
    n = int(lines[0])
    rmin = 0
    rmax = 10e6
    events = []
    for i in range(1, n + 1):
        r1, r2, alpha1, alpha2 = [float(x) for x in lines[i].split()]
        rmin = max(rmin, r1)
        rmax = min(rmax, r2)
        events.append((alpha1, -i))
        events.append((alpha2, i))
    res = intersection_area(events, n, rmax, rmin)
    print("%.6f" % res)