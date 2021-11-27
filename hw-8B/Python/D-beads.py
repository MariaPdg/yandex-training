import sys

sys.setrecursionlimit(2500)


def dfs(now, neighbours, subsize, visited):
    visited[now] = True
    max1 = -1
    max2 = -1
    best = 1
    subsize[now] = 1
    for next in neighbours[now]:
        if not visited[next]:
            best = max(dfs(next, neighbours, subsize, visited), best)
            if subsize[next] > max1:
                max2 = max1
                max1 = subsize[next]
            elif subsize[next] > max2:
                max2 = subsize[next]
    best = max(best, max1 + 1)
    best = max(best, max1 + max2 + 1)
    subsize[now] = max(subsize[now], max1 + 1)
    return best


if __name__ == '__main__':

    """Calculate the maximum length of beads"""

    with open('input.txt', 'r') as file:
        lines = file.readlines()
    n = int(lines[0])
    neighbours = [[] for i in range(n + 1)]
    for i in range(1, n):
        a, b = map(int, lines[i].split())
        neighbours[a].append(b)
        neighbours[b].append(a)
    subsize = [0] * (n + 1)
    visited = [False] * (n + 1)
    print(dfs(1, neighbours, subsize, visited))