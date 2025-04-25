/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getConcatenation(int* nums, int numsSize, int* returnSize) {
    int *concatenatedNums = malloc(numsSize * sizeof(int) * 2); //allocs a array with double space

    *returnSize = numsSize * 2; //gets the size of the new array
    for (int index = 0; index < numsSize; index++)
        concatenatedNums[index] = nums[index]; //fill the new array with the numbers in the same positions
    for (int index = 0; index < numsSize; index++)
        concatenatedNums[index + numsSize] = nums[index]; //fill the new array with the numbers in the new positions
    
    return concatenatedNums;
}
