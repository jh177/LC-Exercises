# merged = []
# 

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        
        merged = []
        
        for interval in intervals:
            if len(merged) == 0: 
                merged.append(interval)
            else:
                prev = merged[-1]
                if interval[0] <= prev[1]:
                    new = [min(prev[0], interval[0]), max(prev[1], interval[1])]
                    merged[-1] = new
                else:
                    merged.append(interval)
        
        return merged