class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        my_set = set()
        for n in nums:
            my_set.add(n)

        t = 1
        for n in nums:
            v, k = 1,1
            m = 1
            while n + k in my_set:
                m += 1
                my_set.discard(n+k)
                k += 1
            while n - v in my_set:
                
                m +=1
                my_set.discard(n-v)
                v +=1
            t = max(t, m)
            

        

        return t