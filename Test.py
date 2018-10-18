# The first line contains a string of length 9. The format is "DDXDDD-DD", where D stands for a digit (non zero)
# and X is an uppercase english letter.
vowels = ["A","E","I","O","U","Y"]
t = input().rstrip()
try:
    vowels.index(t[2])
    print("invalid")
except ValueError:
    for i in range(len(t)):
        if i or i+1 == 2 or 6:
            pass
            print(t[i])
