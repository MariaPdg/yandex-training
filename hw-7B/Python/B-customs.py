def arrived_goods(events):

    events.sort()
    print(events)
    arrived = 0
    max_arrived = 0
    for event in events:
        if event[1] == 1:
            arrived += 1
        elif event[1] == -1:
            arrived -= 1
        max_arrived = max(max_arrived, arrived)
    return max_arrived


if __name__ == '__main__':

    """Define the minimum of machines required for preprocessing all goods after their arrival"""

    n = int(input())
    events = []
    end, start = -1, 1  # out before in
    for i in range(n):
        a, b = map(int, input().split())
        events.append((a, start))
        events.append((a + b, end))
    res = arrived_goods(events)
    print(res)

