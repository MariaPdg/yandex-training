if __name__ == '__main__':

    """Print the auto numbers which correspond to the most number of witness' answers"""

    m = int(input())
    ans = []
    for i in range(m):
        ans.append(set(input().strip()))

    n = int(input())
    autos = []
    max_score = 0
    for i in range(n):
        auto = input().strip()
        autos_set = set(auto)
        score = 0
        for a in ans:
            if a <= autos_set:
                score += 1
        autos.append((auto, score))
        max_score = max(max_score, score)
    res = []
    for auto in autos:
        if auto[1] == max_score:
            print(auto[0])

