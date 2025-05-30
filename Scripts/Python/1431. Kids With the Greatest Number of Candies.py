class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatestAmount = max(candies) # Gets the greates amount by getting the max in the candies list
        result = []

        # Acess all the values in candies list
        for kid in candies:

            # Checks if the current value + the extraCandies is greather or equal the greatestAmount
            if kid + extraCandies >= greatestAmount:
                result.append(True)
            else:
                result.append(False)
        
        return result