class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1: return ["()"]
        
        prev_res = self.generateParenthesis(n-1)
        res = []
        res_set = set()
        
        for ele in prev_res:
            left = "()" + ele
            if left not in res_set:
                res.append(left)
                res_set.add(left)
            
            right = ele + "()"
            if right not in res_set:
                res.append(right)
                res_set.add(right)
            
            for i in range(0, len(ele)-1):
                for j in range(i+1, len(ele)):
                    new_ele = ele[0:i] + "(" + ele[i:j] + ")" + ele[j:]
                        
                    if new_ele not in res_set:
                        res_set.add(new_ele)
                        res.append(new_ele)

        return res