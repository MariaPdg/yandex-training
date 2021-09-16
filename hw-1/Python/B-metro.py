def min_stations(a, b, c):

    """ Tricky case: e.g. from 3 to 9, choose the minimum between 9-3-1 = 5 and 10-9+3-1=3.
        I.e. it is better to go via the stations 10, 1, 2  rather than 4,5,6,7,8"""
    max_n = max(b, c)
    min_n = min(b, c)
    return min(abs(b-c)-1, abs(a - max_n) + min_n - 1)


if __name__ == '__main__':

    """ Find the minimum number of intermediate stations from i to j, 
    n is the total number of stations """

    n, i, j = map(int, input().split())
    res = min_stations(n, i, j)
    print(res)
