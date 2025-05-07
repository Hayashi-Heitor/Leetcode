/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* buildArray(int* nums, int numsSize, int* returnSize) {
    *returnSize = numsSize;

    for(int index = 0; index < numsSize; index++)
        //stores both values at the same element with the in-place approach, using the numsSize as a base
        nums[index] += numsSize * (nums[nums[index] % numsSize] % numsSize);
    
    for(int index = 0; index < numsSize; index++)
        nums[index] /= numsSize; //returns the original value

    return nums;
}