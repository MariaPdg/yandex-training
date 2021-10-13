def build_sorted_map(arr):

    """Builds list with pairs: [item_i, idx_i] where items are unique"""

    dct = {}
    for i, item in enumerate(arr):
        if item not in dct:
            dct[item] = i

    res = [[k, v] for k, v in sorted(dct.items())]
    return res


if __name__ == '__main__':

    """Find i,j,k such that A[i] + B[j] + C[k] = s.
    If several solutions exist output the less one in terms of lexicographic order."""

    s = int(input())
    arrA = [int(x) for x in input().split()]
    arrB = [int(x) for x in input().split()]
    arrC = [int(x) for x in input().split()]
    mapA = build_sorted_map(arrA[1:])
    mapB = build_sorted_map(arrB[1:])
    mapC = build_sorted_map(arrC[1:])

    res = []
    for i in range(len(mapA)):
        j, k = 0, len(mapC)-1
        d = s - mapA[i][0]
        while j < len(mapB) and k >= 0:
            sum_two = mapB[j][0] + mapC[k][0]
            if sum_two > d:
                k -= 1
            elif sum_two < d:
                j += 1
            else:
                res.append([mapA[i][1], mapB[j][1], mapC[k][1]])
                j += 1
                k -= 1
    res = [it for it in sorted(res, key=lambda x: (x[0], x[1], x[2]))]

    if not len(res):
        # if not found
        print(-1)
    else:
        print(*res[0])