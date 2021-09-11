# 1079. Letter Tile Possibilities

# You have n  tiles, where each tile has one letter tiles[i] printed on it.

# Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.

 

# Example 1:

# Input: tiles = "AAB"
# Output: 8
# Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
# Example 2:

# Input: tiles = "AAABBC"
# Output: 188
# Example 3:

# Input: tiles = "V"
# Output: 1

def num_tile_possibilities(tiles)
  poss = []
  (1..tiles.length).each do |i|
    poss = poss | tiles.split("").permutation(i).to_a
  end
  poss.length
end

tiles = "AAABBC"
p num_tile_possibilities(tiles)