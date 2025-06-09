class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # Creates two sets to get rid of duplicates
        set1, set2 = set(nums1), set(nums2)

        # Runs the nums1 list removing the elements that are present in set2 from the sets
        for number in nums1:
            if number in set2:
                set1.remove(number)
                set2.remove(number)
        
        # Returns the sets in a list format
        return [list(set1), list(set2)]
             