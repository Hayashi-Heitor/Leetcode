# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head

        # While the current node != NULL
        while current:
            temp = current.next # Stores the next node
            current.next = previous # Reverses the link
            previous = current # Moves the previous foward to the current position
            current = temp # Moves the current node foward

        return previous # Returns previous because current = NULL