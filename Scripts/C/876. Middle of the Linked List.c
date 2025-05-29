/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* middleNode(struct ListNode* head) {
    // Checks if head is NULL or haves a NULL next
    if(head == NULL || head->next == NULL)
        return head;
    
    // Creates slow and fast pointers
    struct ListNode *slow = head, *fast = head;

    // While fast is not NULL and doesn't have a NULL next we increase slow by 1 and fast by 2
    while(fast != NULL && fast->next != NULL) {
        fast = fast->next->next;
        slow = slow->next;
    }

    return slow; // Returns the slow (half of the fast)
}