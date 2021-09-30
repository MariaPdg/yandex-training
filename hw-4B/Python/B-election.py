if __name__ == '__main__':

    """Calculate the election results"""

    dct = {}
    with open('input.txt') as f:
        lines = f.readlines()

    for item in lines:
        name, n = [x for x in item.split()]
        n = int(n)
        if name not in dct:
            dct[name] = n
        else:
            dct[name] += n
    for k, v in sorted(dct.items()):
        print(k, v)
