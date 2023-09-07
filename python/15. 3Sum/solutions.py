class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i -1 ]:
                continue
            
            l, r = i + 1, len(nums) - 1

            while l < r :
                if num + nums[l] + nums[r] < 0:
                    l += 1
                elif num + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    res.append([num , nums[l] , nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res
