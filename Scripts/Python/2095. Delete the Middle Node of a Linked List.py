# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Checks if head has a link
        if not head.next:
            return None
        
        slow = head
        fast = head

        # While fast and fast.next are not null keeps advancing slow by one and fast by two
        while fast and fast.next:
            fast = fast.next.next 
            link = slow
            slow = slow.next
        
        # When we get to the half changes the link of the previous list
        link.next = slow.next

        return head