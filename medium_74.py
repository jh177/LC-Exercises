def searchMatrix(matrix, target):
    m = len(matrix)
    if m==0: return False
    n = len(matrix[0])

    left = 0
    right = m * n - 1

    while left <= right:
        mid = left + (right - left)//2
        mid_ele = matrix[mid//n][mid%n]
        if mid_ele == target:
            return True
        else:
            if mid_ele > target:
                right = mid - 1
            else:
                left = mid + 1
    
    return False