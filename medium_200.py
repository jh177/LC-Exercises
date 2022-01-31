class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0

        count = 0
        visited = set()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if self.explore(grid, r, c, visited):
                    count += 1

        return count

    def explore(self, grid, r, c, visited):
        row_inbound = r >= 0 and r < len(grid)
        col_inbound = c >= 0 and c < len(grid[0])

        if not row_inbound or not col_inbound:
            return False

        idx = str(r) + '-' + str(c)
        if idx in visited:
            return False
        if grid[r][c] == "0":
            return False

        visited.add(idx)

        self.explore(grid, r+1, c, visited)
        self.explore(grid, r-1, c, visited)
        self.explore(grid, r, c+1, visited)
        self.explore(grid, r, c-1, visited)

        return True
