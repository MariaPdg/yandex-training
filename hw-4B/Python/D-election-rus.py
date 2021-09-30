if __name__ == '__main__':

    """Calculate the election results"""

    with open('input.txt') as f:
        lines = f.readlines()

    votecnt = {}
    places = 450
    first_sum = 0
    for item in lines:
        n = int(item.split()[-1])
        party = ' '.join(item.split()[:-1])
        votecnt[party] = n
        first_sum += n
    first_quat = first_sum / places

    for i, (k, v) in enumerate(votecnt.items()):
            votecnt[k] = [i, v // first_quat]
            places -= v // first_quat
            votecnt[k].append(v % first_quat)
    sorted_cnt = {k: v for k, v in sorted(votecnt.items(), key=lambda x: x[1][2], reverse=True)}
    for k, v in sorted_cnt.items():
        if int(places) > 0:
            sorted_cnt[k][1] += 1
            places -= 1
        else:
            break
    sorted_cnt = {k: v for k, v in sorted(sorted_cnt.items(), key=lambda x: x[1][0])}
    for k, v in sorted_cnt.items():
        print(k, int(v[1]))



