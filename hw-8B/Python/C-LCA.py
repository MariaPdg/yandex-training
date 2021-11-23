def find_lca(tree, n1, n2):

    ancestor = set()
    while n1 in tree:
        ancestor.add(n1)
        n1 = tree[n1]
    ancestor.add(n1)
    while n2 not in ancestor:
        n2 = tree[n2]
    return n2


if __name__ == '__main__':

    """Find a lowest common ancestor (LCA)"""

    with open('input.txt', 'r') as file:
        lines = file.readlines()
    n = int(lines[0])
    tree = {}
    for line in lines[1:n]:
        desc, anc = line.split()
        if desc not in tree:
            tree[desc] = anc
    for line in lines[n:]:
        name1, name2 = line.split()
        ans = find_lca(tree, name1, name2)
        print(ans)
