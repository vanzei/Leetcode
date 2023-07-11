class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setnums = set(nums)
        longest = 0
        for num in nums:
            #if is a start of a sequence no left neighbor
            if (num - 1) not in setnums:
                lenght = 0
                while (num + lenght) in setnums:
                    lenght += 1 
                longest = max(longest , lenght)
        return longest
