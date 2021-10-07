if __name__ == '__main__':

    """Is there a valid number of parentheses in a given sequence?"""

    line = input()
    stack = []
    dct = {'(': 0}
    for s in line:
        if s == '(':
            dct[s] += 1
        elif s == ')':
            dct['('] -= 1
            if dct['('] < 0:
                print('NO')
                exit(0)
    if dct['('] == 0:
        print('YES')
    else:
        print('NO')