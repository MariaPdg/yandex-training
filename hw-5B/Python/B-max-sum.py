def build_prefixsum(nums):
    prefixsum = [0] * (len(nums) + 1)
    for i in range(1, len(nums) + 1):
        prefixsum[i] = prefixsum[i-1] + nums[i-1]
    return prefixsum


if __name__ == '__main__':

    """Find the segment with maximum sum and output max sum"""

    n = int(input())
    arr = [int(x) for x in input().split()]
    prefixsum = build_prefixsum(arr)

    min_elem = 10**9
    max_sum = prefixsum[1]

    for i in range(len(prefixsum)):
        if prefixsum[i] < min_elem:
            min_elem = prefixsum[i]
        elif prefixsum[i] - min_elem > max_sum:
            max_sum = prefixsum[i] - min_elem
    print(max_sum)
