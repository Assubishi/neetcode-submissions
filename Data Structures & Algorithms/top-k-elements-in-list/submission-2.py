class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        ans = []
        sorted_desc = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
        for key, val in sorted_desc.items():
            ans.append(key)
        return ans[0:k]