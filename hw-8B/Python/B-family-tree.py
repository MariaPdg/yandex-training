from copy import deepcopy


def family_tree(tree, n1, n2):

    name1_prev = deepcopy(n1)
    name2_prev = deepcopy(n2)
    while n2 in tree:
        n2 = tree[n2]
        if n2 == name1_prev:
            return 1
    if n2 != name1_prev:
        if n1 in tree:
            while n1 in tree:
                n1 = tree[n1]
                if name2_prev == n1:
                    return 2
    return 0


if __name__ == '__main__':

    """Build a family tree from pairs [a, b]:
       return:
        1: if a is an ancestor of b
        2: if b is an ancestor of a
        otherwise 0"""

    with open('input.txt', 'r') as file:
        lines = file.readlines()
    n = int(lines[0])
    tree = {}
    ans = []
    for line in lines[1:n]:
        desc, anc = line.split()
        if desc not in tree:
            tree[desc] = anc
    for line in lines[n:]:
        name1, name2 = line.split()
        if name2 in tree:
            res = family_tree(tree, name1, name2)
        elif name1 in tree:
            if name1 in tree:
                res = family_tree(tree, name1, name2)
        elif not res:
                res = family_tree(tree, name2, name1)
        ans.append(res)
    print(*ans)
