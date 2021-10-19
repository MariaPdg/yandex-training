if __name__ == '__main__':

    """n = number of points, k = number of segments
       Calculate the minimum l such that each point is covered by a segment of length l"""

    n, k = map(int, input().split())
    points = [int(x) for x in input().split()]
    points.sort()
    left = 0
    right = points[-1] - points[0]
    while left < right:
        l = (left + right) // 2
        max_right = points[0] - 1
        count = 0
        for p in points:
            if p > max_right:
                count += 1
                max_right = p + l
        if count > k:
            left = l + 1
        else:
            right = l
    print(left)
