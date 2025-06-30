# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        previous = None

        # Takes the slow pointer to the half of the linked lists
        while fast and fast.next:

            # Stores the next slow value and advances the fast
            temp = slow.next
            fast = fast.next.next

            # Inverses the next of the current slow pointer to the previous
            slow.next = previous
            previous = slow
            slow = temp
        
        # Gets the sum of the two twins one of each half and compares with the maxTwin
        maxTwin = 0
        while slow:
            maxTwin = max(maxTwin, previous.val + slow.val)
            previous = previous.next
            slow = slow.next
        
        return maxTwin
