def distance(d, x, y, vertex):

    """ The function to find distance to the vertex """

    if vertex == 1:
        a, b = x, y

    elif vertex == 2:
        a = abs(x-d)
        b = y

    elif vertex == 3:
        b = abs(y-d)
        a = x

    return a**2 + b**2


def check_location(d, x, y):

    if -x + d >= y >= 0 and x >= 0:  # (x, y) is inside the triangle
        return 0
    dist = [distance(d, x, y, 1), distance(d, x, y, 2), distance(d, x, y, 3)]
    return dist.index(min(dist)) + 1


if __name__ == '__main__':

    """ Determine the relevant position of the point (x, y) and the triangle with the vertices: 
    A(0,0), B(d, 0), C(0, d)"""

    d = int(input())
    x, y = map(int, input().split())
    res = check_location(d, x, y)
    print(res)