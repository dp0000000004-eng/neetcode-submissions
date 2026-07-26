class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # return ("".join(sorted(s)) == "".join(sorted(t)))

        a = {}
        b = {}

        for i, w in enumerate(sorted(s)):
            a[i] = w
        for i, w in enumerate(sorted(t)):
            b[i] = w

        ans = True

        for i in range(len(max(s, t))):
            try:
                if a[i] == b[i]:
                    continue
                else:
                    ans = False
            except KeyError:
                ans = False
                break

        return ans