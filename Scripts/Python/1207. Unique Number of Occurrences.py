class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # Create a numbers set to get rid of duplicates
        numbers = set(arr)
        appearences = set()

        # Checks all the numbers in the numbers set
        for number in numbers:

            # If the amount has already been seen returns false
            if arr.count(number) in appearences:
                return False
            
            # Else adds the value to the numbers appearences set
            appearences.add(arr.count(number))
        
        return True
