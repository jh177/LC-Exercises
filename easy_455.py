def findContentChildren(g, s):
        g.sort()
        s.sort()
        
        count = 0
        
        i = 0
        j = 0
        
        while j < len(s) and i < len(g):
            if s[j] >= g[i]:
                count += 1
                i += 1
            j += 1
            
        return count