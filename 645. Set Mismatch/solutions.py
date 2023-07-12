class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        check = [_ for _ in range(1,len(nums)+1)]
        for value in check:
            if value in nums:
                continue
            else:
                uniques = []
                for num in nums:
                    if num not in uniques:
                        uniques.append(num)
                    else:
                        return [num, value]
