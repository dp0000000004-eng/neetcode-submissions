import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^A-Za-z0-9]', '', s).lower()
        
        
        k = len(s) - 1
        ans = True

        for i in range(len(s)):
            if s[i] == s[k]:
                k -= 1
                continue
            else:
                ans = False

        return ans