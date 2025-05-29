/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
void deleteNode(struct ListNode* node) {
    node->val = node->next->val; // Gets the next node value and attributes to the current node

    // Creates a temp value to free the next node from the memory
    struct ListNode *tempFreeNode = node->next;
    node->next = node->next->next; // Atributes the next node from the next to the current
    free(tempFreeNode);
}