def count_cats(events, segments):

    events.sort()
    count = 0
    for event in events:
        if event[1] == -1:
            segments[event[2]][2] = count
        elif event[1] == 1:
            segments[event[2]][2] = count - segments[event[2]][2]
        else:
            count += 1
    return [elem[2] for elem in segments]


if __name__ == '__main__':

    """The problem is about cats, reformulation: 
    How many points (arr) does each segment (events[i]) cover?
    Events:
        -1: segment starts
         1: segment ends
         0: cat appears
    Idea: if event[i] == 0 => increase cat counter: count += 1
          if event[i] == -1 => segments[event[i]][2] = count
          if event[i] == 1 => segments[event[i]][2] = count - segments[event[2]][2]: 
          current cat number - previous cat number"""

    with open('input.txt', 'r') as file:
        lines = file.readlines()
    n, m = map(int, lines[0].split())
    events = [(0, 0, 0)] * (2 * m + n)  # cats + segments (x 2: start, end)
    cats = [int(x) for x in lines[1].split()]
    segments = [[0, 0, 0]] * m  # l, r, cat_count
    start, end, cat_event = -1, 1, 0
    i = 0
    for c in cats:
        events[i] = (c, cat_event, -1)
        i += 1

    idx = 2
    for j in range(m):
        l, r = map(int, lines[idx].split())
        events[i] = (l, start, j)
        events[i+1] = (r, end, j)
        segments[j] = [l, r, 0]
        i += 2
        idx += 1
    for i in range(2, m+2):
        l, r = map(int, lines[i].split())

    res = count_cats(events, segments)
    print(*res)

