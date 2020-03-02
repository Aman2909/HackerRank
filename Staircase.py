def staircase(n):
    for i in range(n):
        for j in range(n - i- 1):
            print(j, end='')
        for j in range(i + 1):
            print("#", end='')
        print("")

staircase(9)