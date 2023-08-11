class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        setnumns = set(nums)
        uniques = list(setnumns)
        uniques.sort(reverse=True)
        if len(uniques) < 3:
            return uniques[0]
        else:
            return uniques[2]
