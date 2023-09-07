class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [1 for _ in range(len(nums))]
        leftA = [1 for _ in range(len(nums))]
        rightA = [1 for _ in range(len(nums))]

        product = 1
        for num in range(len(nums)):
            leftA[num] = product
            product *= nums[num]

        product = 1
        for num in reversed(range(len(nums))):
            rightA[num] = product
            product *= nums[num]
       
        for value in range(len(nums)):
            products[value] = leftA[value] * rightA[value]
        
        return products
