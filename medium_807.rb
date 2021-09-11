require "byebug"

# 807. Max Increase to Keep City Skyline

# Input: grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
# Output: 35
# Explanation: The building heights are shown in the center of the above image.
# The skylines when viewed from each cardinal direction are drawn in red.
# The grid after increasing the height of buildings without affecting skylines is:
# gridNew = [ [8, 4, 8, 7],
#             [7, 4, 7, 7],
#             [9, 4, 8, 7],
#             [3, 3, 3, 3] ]

def max_increase_keeping_skyline(grid)
  row, col = grid.length, grid.first.length
  w_max = grid.map {|row| row.max}
  n_max = grid.transpose.map {|col| col.max}
  count = 0
  (0...row).each do |r|
    (0...col).each do |c|
      count += [w_max[r]-grid[r][c], n_max[c]-grid[r][c]].min
    end
  end
  count
end


grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
p max_increase_keeping_skyline(grid)