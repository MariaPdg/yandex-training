def max_min_distance(nums):

    shops = [i for i in range(len(nums)) if nums[i] == 2]
    houses = [i for i in range(len(nums)) if nums[i] == 1]
    res = []
    for h in houses:
        dist = []
        for s in shops:
            dist.append(abs(s-h))
        res.append(min(dist))
    return max(res)


if __name__ == '__main__':

    """ Input of n numbers: e.g. 2 0 1 1 0 1 0 2 1 2, where 0-offices, 1-houses, 2-shops.
        Define the maximum between the minimum distances from houses to shops """

    street = [int(x) for x in input().split()]
    res = max_min_distance(street)
    print(res)