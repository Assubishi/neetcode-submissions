class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        f = Counter(s)
        q = Counter(t)

        for n in f.keys():
            if f[n] != q[n]:
                return False

        return True 