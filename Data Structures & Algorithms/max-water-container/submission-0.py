class Solution:
    def maxArea(self, heights: List[int]) -> int:
        f, l = 0, len(heights) -1
        d = len(heights) - 1
        m = 0
        while f < l:
            h = min(heights[f], heights[l])
            w = h * d
            m = max(m, w)

            if h == heights[f]:
                f += 1
            else:
                l -= 1
            d -= 1
        return m
