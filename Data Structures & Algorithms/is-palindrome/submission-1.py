class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return False
        t = "".join(char for char in s if char.isalnum()).lower()
        f, l = 0, len(t)-1
        while f < l:
            if t[f] != t[l]:

                return False
            f += 1
            l -= 1
        return True