def maxArea(height):

    l = 0
    r = len(height)-1

    max_area = 0

    while l < r:
        max_l = height[l]
        max_r = height[r]
        area = min(max_l, max_r) * (r-l)
        max_area = max(max_area, area)

        if height[l] < max_r:
            l += 1
        elif height[r] < max_l:
            r -= 1  
        else:
            l += 1
            r -= 1

    return max_area


height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))