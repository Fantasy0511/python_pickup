from math import sqrt

for n in range(101, 0, -1):
    root = sqrt(n)
    if root == int(root):
        break
    else:
        print('hello')
