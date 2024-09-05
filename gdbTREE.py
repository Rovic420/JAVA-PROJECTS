import sys

def tree(height):
    for curr_n in range(1, height+1):
        print(' '*(height-curr_n) + '*'*(2*curr_n-1))
        sys.stdout.flush()

tree(9)
