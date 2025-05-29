/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteDuplicates(struct ListNode* head) {
    struct ListNode *currentNode = head;

    // While current node and the next node are not NULL
    while(currentNode && currentNode->next) {

        // If current node and the next have the same value delete the next node and free the memory
        if(currentNode->val == currentNode->next->val) {
            struct ListNode *tempFree = currentNode->next;
            currentNode->next = currentNode->next->next;
            free(tempFree);
        }
        
        // Else just go to the next node
        else
            currentNode = currentNode->next;
    }

    return head;
}