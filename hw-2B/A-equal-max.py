def equal_to_max(arr):

    cnt = {}
    for item in arr:
        if item not in cnt:
            cnt[item] = 0
        cnt[item] += 1
    max_el = max(list(cnt.keys()))
    return cnt[max_el]


if __name__ == '__main__':

    "Calculate the number of values in a sequence, which are equal to the maximum value"

    nums = []
    while True:
        x = int(input())
        if x != 0:
            nums.append(x)
        else:
            break
    res = equal_to_max(nums)
    print(res)
