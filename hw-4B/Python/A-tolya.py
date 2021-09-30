if __name__ == '__main__':

    """Calculate the sum of numbers i with the color d"""

    n = int(input())
    dct = {}
    for i in range(n):
        d, i = map(int, input().split())
        if d not in dct:
            dct[d] = i
        else:
            dct[d] += i
    for k, v in sorted(dct.items()):
        print(k, v)
