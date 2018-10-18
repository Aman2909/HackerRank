# John works at a clothing store. He has a large pile of socks that he must pair by color for sale. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.
#
# For example, there are  socks with colors . There is one pair of color  and one of color . There are three odd
# socks left, one of each color. The number of pairs is .
#
# Function Description
#
# Complete the sockMerchant function in the editor below. It must return an integer representing the number of matching pairs of socks that are available.
#
# sockMerchant has the following parameter(s):
#
# n: the number of socks in the pile
# ar: the colors of each sock
# Input Format
#
# The first line contains an integer , the number of socks represented in .
# The second line contains  space-separated integers describing the colors  of the socks in the pile.
#
# Constraints
#
#  where
# Output Format
#
# Print the total number of matching pairs of socks that John can sell.
#
# Sample Input
#
# 9
# 10 20 20 10 10 30 50 10 20
# Sample Output
#
# 3
# Explanation
#
# John can match three pairs of socks.


# !/bin/python3


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    socks=0
    hash=[0]*100
    for x in ar:
        hash[x-1]+=1
    for x in hash:
        socks+=x//2
    return socks

ar=[1,2,3,3,4,5,3,1,2,1,2,1,1,1,1,5,6,1,1]
n=len(ar)
y=sockMerchant(n,ar)
print(y)