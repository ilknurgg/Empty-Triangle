n =10

def do_star(x):

    inner = 0
    outter =0
    i = 0
    j = 0
    inner = -1
    outter = x-1

    i = 1

    while i<=x-1:
        if i!=x:
            for j in range(1, outter + 1):
                print(" ", end = '')
            print("*", end = '')

        if i!=1:

            for j in range(1, inner + 1):
                print(" ", end = '')
            print("*", end = '')

        inner+=2
        outter -= 1
        print("\n", end = '')

        i += 1
    if i == x:  
        print("*", (" " * (inner-2)),"*", end='')


do_star(n)
