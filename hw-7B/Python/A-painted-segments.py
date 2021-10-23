def painted_segments(segments):

    segments.sort()
    painted_len = 0
    online = 0
    for i in range(len(segments)):
        if online > 0:
            painted_len += segments[i][0] - segments[i-1][0]
        if segments[i][1] == -1:
            online += 1
        else:
            online -= 1
    return painted_len


if __name__ == '__main__':

    """Given N segments (a, b) define the length of the painted segments"""

    n = int(input())
    segments = []
    start, end = -1, 1  # start is before end
    for i in range(n):
        a, b = map(int, input().split())
        segments.append((a, start))
        segments.append((b, end))
    res = painted_segments(segments)
    print(res)

