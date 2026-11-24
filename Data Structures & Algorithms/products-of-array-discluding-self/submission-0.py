class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        f = []
        s = []
        # 1 1 2 8
        # 1 6 24 48
        for i in range(len(nums)):
            if i == 0:
                f.append(1)
                continue
            f.append(f[i-1] * nums[i-1])
        temp = len(nums) 
        q = 0
        while temp >=0:
            
            if temp == len(nums):
                s.append(1)
                temp -= 1
                continue
            s.append(nums[temp] * s[q])
            q+=1
            temp -=1
            
        
        j = len(nums)-1
        for i in range(len(f)):
            f[i] = f[i] * s[j]
            j -= 1
        
        return f

