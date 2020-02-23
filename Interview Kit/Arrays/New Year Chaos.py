def minimumBribes(q):
    for i in range(len(q)):
        if not abs(q[i]-i)<=3:
            return "Too chaotic"
    test=[i for i in range(1,len(q))]
    for i in range (len(q),0):
        test[i]


t = int(input())
for t_itr in range(t):
    n = int(input())
    q = list(map(int, input().rstrip().split()))

    minimumBribes(q)
