# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode() #creates a dummy linked list
        carry = 0
        current = dummy #creates a pointer for the dummy list
        while l1 or l2 or carry: #while there's still numbers on the lists or there's still a carry
            sum = carry #adds the carry to the current sum
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            carry = sum // 10 #gets the digits > 9 of the sum and pass it to the carry
            current.next = ListNode(sum % 10) #pass the rest of the sum to the current dummy list
            current = current.next
        return dummy.next
