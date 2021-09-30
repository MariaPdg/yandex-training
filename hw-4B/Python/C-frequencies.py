def sort_frequencies(dct):

    sorted_by_value = [(k, v) for k, v in sorted(dct.items(), key=lambda x: (x[1]), reverse=True)]
    dct = {}
    for item in sorted_by_value:
        if item[1] not in dct:
            dct[item[1]] = []
        dct[item[1]].append(item[0])

    return dct


if __name__ == '__main__':

    """Sort words from the text by frequency and in alphabet order if frequencies are equal"""

    dct = {}
    with open('input.txt') as f:
        lines = f.readlines()

    for item in lines:
        words = [x for x in item.split()]
        for w in words:
            if w not in dct:
                dct[w] = 0
            dct[w] += 1
    sorted_dct = sort_frequencies(dct)
    for k, v_list in sorted_dct.items():
        print('\n'. join(sorted(v_list)))