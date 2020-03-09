code = '''def alternatingCharacters(s):
    dels = 0
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            dels+=1
    return dels
'''
# qwerty =['AAAA','BBBBB','ABABABAB','BABABA','AAABBB']
# for i in qwerty:
#     print(alternatingCharacters(i))

import timeit
time = timeit.timeit(stmt=code,setup = "s =['AAAA','BBBBB','ABABABAB','BABABA','AAABBB']",number = 1000000)
print(time)