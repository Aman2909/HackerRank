# DONE

ar = list(map(int,'10 20 20 10 10 30 50 10 20'.split(' ')))
counter = {}
for i in ar:
    if str(i) not in counter:
        counter[str(i)] = 1
    else:
        counter[str(i)] += 1
sum = 0
for i in counter.values():
    sum += i // 2
print(sum)