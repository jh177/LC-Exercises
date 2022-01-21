def maxArea(height):
    max_area = 0

    l = 0
    r = len(height)-1

    while l < r:
        max_l = height[l]
        max_r = height[r]
        h = min(max_l, max_r)
        area = h * (r-l)
        
        if (area > max_area): 
            max_area = area
        
        if (max_l < max_r):
            l += 1
        else:
            r -= 1
        
    return max_area


print(maxArea([1,8,6,2,5,4,8,3,7]))
print(maxArea([1,3,2,5,25,24,5]))