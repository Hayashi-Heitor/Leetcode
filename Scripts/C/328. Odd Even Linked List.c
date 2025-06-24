/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* oddEvenList(struct ListNode* head) {

    // If there are more than 2 elements in the list
    if (head != NULL && head->next != NULL) {
        // Creates the odd, even and head of the even struct pointers
        struct ListNode *odd = head, *even = head->next, *evenHead = even;

        // While there are more than 2 elements in even
        while (even != NULL && even->next != NULL) {

            // Gets the next odd and even
            odd->next = odd->next->next;
            even->next = even->next->next;
            
            // Updates current odd, even
            odd = odd->next;
            even = even->next;
        }

        // Stitches the even head at the end of the odd
        odd->next = evenHead;
    }
    
    return head;
}