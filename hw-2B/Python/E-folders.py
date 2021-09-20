def minimum_time(arr):

    return sum(sorted(arr)[:-1])


if __name__ == "__main__":

    """Calculate the minimum time required to find the diploma in folders in the worst case (1 sec per diploma).
       Input: n = number of folders, arr = number of diplomas in each folder. """

    n = int(input())
    arr = [int(x) for x in input().split()]
    res = minimum_time(arr)
    print(res)