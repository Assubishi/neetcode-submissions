class Solution:

    def encode(self, strs: List[str]) -> str:
        ans  =  str(len(strs))
        for s in strs:
            ans += "!>>" + s  
        return ans

    def decode(self, s: str) -> List[str]:
        ans = s.split("!>>")
        print(ans)
        return ans[1:len(ans)]
