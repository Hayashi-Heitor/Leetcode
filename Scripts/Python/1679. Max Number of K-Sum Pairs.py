class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        differences = {} 
        maximumOperations = 0

        # Searches all the array and get each complement
        for num in nums:
            complement = k - num

            # If the complement exists in the dict, increase the maximumOperations and remove it
            if complement in differences and differences[complement] > 0:
                maximumOperations += 1
                differences[complement] -= 1
            
            # Else add the num to the differences dict
            else:
                differences[num] = differences.get(num, 0) + 1
        
        return maximumOperations