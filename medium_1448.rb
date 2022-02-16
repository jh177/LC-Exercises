# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val = 0, left = nil, right = nil)
#         @val = val
#         @left = left
#         @right = right
#     end
# end
# @param {TreeNode} root
# @return {Integer}

# bfs, queue track node in each level
# for each node, dfs

def good_nodes(root)
    stack = [[root, -Float::INFINITY]]
    count = 0
    
    while !stack.empty?
        node, max_so_far = stack.pop()
        
        if max_so_far <= node.val
            count += 1
        end
        
        if !node.left.nil?
            stack.append([node.left, [node.val, max_so_far].max])
        end

        if !node.right.nil?
            stack.append([node.right, [node.val, max_so_far].max])
        end
        
    end
    
    return count
end