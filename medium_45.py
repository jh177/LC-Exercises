def can_jump(nums)
    count = 0
    current_end = 0
    max_jump = 0

    for i in range(len(nums)-1):
      max_jump = max(max_jump, i+nums[i])
      if i == current_end:
        count += 1
        current_end = max_jump

    return count