def count_matches(arr1, arr2):

    return len(set(arr1) & set(arr2))


if __name__ == '__main__':

    """ Count the number of matches in list1 and list2"""

    list1 = [int(x) for x in input().split()]
    list2 = [int(x) for x in input().split()]
    res = count_matches(list1, list2)
    print(res)
