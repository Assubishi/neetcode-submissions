class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
        ans = []
        for s in strs:
            need = "".join(sorted(s))
            if need in d:
                d[need].append(s)
            else:
                d[need] = [s] 
        
        for val in d.values():
            ans.append(val)
            
        return ans