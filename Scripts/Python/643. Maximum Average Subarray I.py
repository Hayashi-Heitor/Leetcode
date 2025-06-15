class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currentSum = sum(nums[:k])
        maximumNumber = currentSum

        # Starting at the k element we check every element in the list
        for index in range(k, len(nums)):

            # We increade the right element and decrease the left elemnt from the currentSum
            currentSum += nums[index] - nums[index - k]

            # if the currentSum is bigger then the maximumNumber we make it the new maximum
            if currentSum > maximumNumber:
                maximumNumber = currentSum

        # returns the average of the maximumNumber
        return maximumNumber / float(k)