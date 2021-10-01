if __name__ == '__main__':

    """Output the most frequent topic"""

    with open('input.txt') as f:
        lines = f.readlines()

    cnt = {}
    n = int(lines[0])
    i = 0
    message = 1
    for i in range(len(lines[1:])):
        if lines[i].split('\n')[0].isdigit():
            if int(lines[i]) == 0:
                topic = lines[i+1]
                if topic not in cnt:
                    cnt[topic] = [message]
                    message += 1
            else:
                for k, v in cnt.items():
                    if int(lines[i]) in v:
                        cnt[k].append(message)
                        message += 1
    # sort by number of messages
    sorted_cnt = {k: v for k, v in sorted(cnt.items(), key=lambda x: len(x[1]), reverse=True)}
    print(list(sorted_cnt.keys())[0])

