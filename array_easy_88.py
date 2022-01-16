def merge(nums1, m, nums2, n):
    result = []

    left = nums1[:m]
    right = nums2[:n]

    while len(left) > 0 and len(right)>0:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    
    result = result + left + right
    
    for i in range(m+n):
        nums1[i] = result[i]

    return nums1


print(merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3))
