#DONE!

from collections import deque
#a=[33,4,11,100000,23,11,33,55,33,22]
# b=deque(a)
# x=b.popleft()
# b.append(x)
# print(b)
# print(type(b))
# c=[]
# c=list(b)
# print(c)
# print(type(c))


def rotLeft(a, d):
    for i in range(d):
        a=deque(a)
        x=a.popleft()
        a.append(x)
    return list(a)
a = list(map(int, input().rstrip().split()))
d=10
result = rotLeft(a,d)
print(result)


