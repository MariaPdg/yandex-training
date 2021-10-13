def read_and_enum():

    arr = list(map(int, input().split()))
    for i in range(len(arr)):
        arr[i] = (arr[i], i + 1)
    arr.sort()
    return arr


if __name__ == '__main__':

    """Find class room with y_i computers for student groups where x_i students, such that 
    x_i + 1 <= y_i (+1 computer for teacher)"""

    n, m = map(int, input().split())
    x = read_and_enum()
    y = read_and_enum()

    groups = [0] * (n+1)
    count = 0
    ynum = 0

    for students, idx in x:
        while ynum < len(y) and y[ynum][0] < students + 1:
            ynum += 1
        if ynum == len(y):
            break
        groups[idx] = y[ynum][1]
        count += 1
        ynum += 1

    print(count)
    print(*groups[1:])
