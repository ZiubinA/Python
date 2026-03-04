def diagonalDifference(arr):
    n = len(arr)
    primary_sum = 0
    secondary_sum = 0
    
    for i in range(n):
        primary_sum += arr[i][i]
        secondary_sum += arr[i][n - 1 - i]
        
    return abs(primary_sum - secondary_sum)

arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

print(diagonalDifference(arr))