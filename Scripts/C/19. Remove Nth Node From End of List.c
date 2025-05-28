/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {

    // Checks if the list contains only one node or its empty
    if(head->next == NULL || head == NULL)
        return NULL;

    // Creates a dummy for border cases and the fast / slow node pointers
    struct ListNode dummy = {0, head};
    struct ListNode *fast = &dummy, *slow = &dummy;
    
    // Advances the fast pointer n + 1 times
    for(int index = 0; index <= n; index++)
        fast = fast->next;

    // Gets the slow pointer to be behind the node we want to remove
    while(fast) {
        fast = fast->next;
        slow = slow->next;
    }

    // Removes the node and clears him from the memory
    struct ListNode *freeAux = slow->next;
    slow->next = slow->next->next;
    free(freeAux);

    // Returns the new head
    return dummy.next;
}