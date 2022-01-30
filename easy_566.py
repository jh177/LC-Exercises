class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        if m*n != r*c:
            return mat

        flat_mat = []
        for row in mat:
            for ele in row:
                flat_mat.append(ele)

        res = [[0 for y in range(c)] for x in range(r)]

        for x in range(r):
            for y in range(c):
                res[x][y] = flat_mat.pop(0)

        return res
