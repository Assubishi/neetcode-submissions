class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i in range(len(nums)):
            if nums[i] in d and target - nums[i] == nums[i]:
                return [d[nums[i]], i]
            else:
                d[nums[i]] = i
        
        for n in d.keys():
            if target - n in d and target -n != n:
                return [d[n], d[target-n]]
        return None