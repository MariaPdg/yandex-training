import math


def distance(d, x, y, vertex):

    """ The function to find distance to the vertex """

    if vertex == 1:
        a, b = x, y

    elif vertex == 2:
        if x * d < 0:
            a = abs(x) + abs(d)
        else:
            a = max(abs(x), abs(d)) - min(abs(x), abs(d))
        b = y

    elif vertex == 3:
        if y * d < 0:
            b = abs(y) + abs(d)
        else:
            b = max(abs(y), abs(d)) - min(abs(y), abs(d))
        a = x

    return math.sqrt(a**2 + b**2)


def check_location(d, x, y):

    if -x + d >= y >= 0 and x >= 0:  # (x, y) is inside the triangle
        return 0
    dist = [distance(d, x, y, 1), distance(d, x, y, 2), distance(d, x, y, 3)]
    min_dist = min(dist)
    rep = 0  # check the equal distances
    for c in dist:
        if c == min_dist:
            rep += 1
    if rep == 1:  # all distances are unique
        return dist.index(min_dist) + 1
    else:
        for i, c in enumerate(dist):
            # return the earliest vertex
            if c == min_dist:
                return i + 1


if __name__ == '__main__':

    """ Determine the relevant position of the point (x, y) and the triangle with the vertices: 
    A(0,0), B(d, 0), C(0, d)"""

    d = int(input())
    x, y = map(int, input().split())
    res = check_location(d, x, y)
    print(res)