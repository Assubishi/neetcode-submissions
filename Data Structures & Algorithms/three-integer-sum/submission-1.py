class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if  i > 0 and nums[i] == nums[i-1]:
                continue
            f = i + 1
            l = len(nums) - 1
            if f == l:
                break
            while f < l:
                temp = nums[i] + nums[f] + nums[l] 
                if temp == 0:
                    if nums[f] == nums[f-1] and l < len(nums) -1 and nums[l] == nums[l+1]:
                        l-=1
                        f+=1
                        continue
                    ans.append([nums[i], nums[f], nums[l]])
                    l-=1
                    f+=1
                elif temp > 0 :
                    l -= 1
                else:
                    f += 1
            
                

            
        return ans