class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my = Counter(nums)
        for n in my.values():
            if n>1:
                return True
        return False