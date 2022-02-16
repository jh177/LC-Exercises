def can_jump(nums)
    max_reach = nums[0]
    end_index = nums.length-1
    
    if max_reach >= end_index
        return true
    end
        
    (1..end_index).each do |i|
        return false if i > max_reach
        max_reach = [max_reach, i+nums[i]].max

        return true if max_reach >= end_index

    end
    
    false
    
end