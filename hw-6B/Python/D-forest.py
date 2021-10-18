if __name__ == '__main__':

    """Person 1: A = the number of trees to cut in each day, each Kth day is holiday.
       Person 2: B = the number of trees to cut in each day, each Mth day is holiday.
       X = the number of trees.
       How many day are required to cut all trees?"""

    a, k, b, m, x = map(int, input().split())
    l = 0
    r = x * 2 // a + 1  # max days if person 1 works alone and has a holiday one per 2 days (k = 2)
    while l < r:
        days = (l + r) // 2
        hd1 = days // k
        hd2 = days // m
        if (days - hd1) * a + (days - hd2) * b < x:
            l = days + 1
        else:
            r = days
    print(l)
