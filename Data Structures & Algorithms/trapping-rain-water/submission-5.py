class Solution:
    def trap(self, height: List[int]) -> int:
        f,s = 0, 1
        ans = 0
        temp = 0
        arr = []
        brr = []
        l = len(height) - 1
        for i in range(len(height)):
            if i == 0 :
                arr.append(0)
                brr.append(height[l])
            else:
                arr.append(max(height[i-1], arr[i-1]))
                brr.append(max(brr[i-1], height[l-i]))
        
        
        for i in range(len(height)):
            ans += max(min(arr[i], brr[l-i]) - height[i], 0)
            
            
        return ans