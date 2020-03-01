def diagonal_difference(arr):
    n = len(arr)
    x=y=0
    for i in range(n):
        x +=arr[i][i]
        y += arr[i][n - 1 - i]
    return abs(x-y)

b = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
arr = [[1, 2, 3, 7], [4, 5, 6, 9], [7, 8, 9, 7], [4, 5, 6, 7]]
f = diagonal_difference(arr=b)
print(f)
