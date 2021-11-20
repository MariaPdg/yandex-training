class BinaryTree(object):

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def print_tree(self, depth=0):
        if not self.data:
            return 0
        if self.left:
            self.left.print_tree(depth+1)
        print('.' * depth + str(self.data))
        if self.right:
            self.right.print_tree(depth+1)

    def add(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = BinaryTree(data)
                else:
                    self.left.add(data)
                    return 0
            elif data > self.data:
                if self.right is None:
                    self.right = BinaryTree(data)
                else:
                    self.right.add(data)
                    return 0
            else:
                print('ALREADY')
                return 0
        else:
            self.data = data
        print('DONE')
        return 0

    def search(self, data):

        if not self.data:
            print('NO')
            return 0

        if data < self.data:
            if self.left is None:
                print('NO')
                return 0
            return self.left.search(data)
        if data > self.data:
            if self.right is None:
                print('NO')
                return 0
            return self.right.search(data)
        else:
            print('YES')
        return 0


if __name__ == '__main__':

    """Implement binary tree with the functions: ADD, SEARCH, PRINTTREE"""

    binary_tree = BinaryTree(None)

    with open('input.txt', 'r') as file:
        lines = file.readlines()
    for line in lines:
        if line == 'PRINTTREE\n':
            binary_tree.print_tree()
        else:
            func, num = line.split()
            num = int(num)
            if func == 'ADD':
                binary_tree.add(num)
            elif func == 'SEARCH':
                binary_tree.search(num)
