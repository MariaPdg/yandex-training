def build_prefixsum(nums):
    prefixsum = [0] * (len(nums) + 1)
    for i in range(1, len(nums) + 1):
        prefixsum[i] = prefixsum[i-1] + nums[i-1]
    return prefixsum


def segment_sum(prefixsum, l, r):
    return prefixsum[r] - prefixsum[l-1]


if __name__ == '__main__':

    """ Calculate prefix sums for segments [l, r] of the array"""

    n, q = map(int, input().split())
    arr = [int(x) for x in input().split()]
    segments = []
    for i in range(q):
        l, r = map(int, input().split())
        segments.append((l, r))
    prefixsum = build_prefixsum(arr)
    for l, r in segments:
        print(segment_sum(prefixsum, l, r))

