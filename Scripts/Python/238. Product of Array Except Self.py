class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lenght = len(nums)

        # Creates a products array with the size of the nums array
        products = [1] * lenght

        # Chechs all the values from the left and adds them to the products array
        for index in range(1, lenght):
            products[index] = products[index-1] * nums[index-1]
        
        # Adds the values from the right to the products array
        right = nums[-1]
        for index in range(lenght-2, -1, -1):
            products[index] *= right
            right *= nums[index]
        
        # Returns the array
        return products