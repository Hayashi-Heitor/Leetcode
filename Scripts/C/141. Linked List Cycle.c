/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool hasCycle(struct ListNode *head) {
    
    // Creates 2 structs from the head for the Floyd's Cycle-Finding Algorithm
    struct ListNode *fast = head;
    struct ListNode *slow = head;

    // While fast and it's next list are not NULL we keep advancing
    while(fast != NULL && fast->next != NULL) {
        slow = slow->next;
        fast = fast->next->next;

        // If both slow and fast are equal the list has a cycle
        if(slow == fast)
            return true;
    }

    // If not we searched all of it or it was a null list
    return false;
}