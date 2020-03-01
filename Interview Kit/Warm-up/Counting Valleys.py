def countingValleys(n, s):
    o = {
        'D':-1,
        'U':1
    }
    height = valley = 0
    for i in s:
        height += o[i]
        if height == 0 and i == 'U':
            valley +=1
    return (valley)

n = int(input())
s = input()

countingValleys(n,s)