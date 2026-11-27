class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        m = 1
        my_d = dict()
        f = 0
        for i in range(len(s)):
            if s[i] not in my_d:
                my_d[s[i]] = i
                m = max(m, i -f + 1)
            else:
                f = max(f, my_d[s[i]] + 1)  
                my_d[s[i]] = i             
                m = max(m, i - f + 1)       
           
                
        return m