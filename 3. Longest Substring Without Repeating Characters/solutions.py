class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        uniques = set()
        maxL = 0

        for r in range(len(s)):
            while s[r] in uniques:
                uniques.remove(s[l])
                l += 1
            uniques.add(s[r])
            maxL = max(maxL, r - l + 1)
        return maxL
