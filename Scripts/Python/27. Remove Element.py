class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        aux = 0
        for index in range(len(nums)):
            if nums[index] != val: #checks if the main pointer is not equal to the val
                nums[aux] = nums[index] #changes the number from the original pointer to the aux
                aux += 1 
        return aux #returns all the times the numbers were swapped
