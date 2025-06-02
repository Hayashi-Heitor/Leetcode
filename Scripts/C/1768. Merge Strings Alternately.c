char * mergeAlternately(char * word1, char * word2){
    int indexWord1 = 0, indexWord2 = 0, indexResult = 0;
    // Aloccates enough space to both the words and the final '\0'
    char *result = malloc(strlen(word1) + strlen(word2) + 1);

    // Intercalates word1 and word2 while there are still letter in both words
    while(indexWord1 < strlen(word1) && indexWord2 < strlen(word2)) {
        result[indexResult++] = word1[indexWord1++];
        result[indexResult++] = word2[indexWord2++];
    }

    // If there are still letters in word1 appends it to the end of the result
    while(indexWord1 < strlen(word1))
        result[indexResult++] = word1[indexWord1++];
    
    // If there are still letters in word2 appends it to the end of the result
    while(indexWord2 < strlen(word2))
        result[indexResult++] = word2[indexWord2++];
    
    // Adds the '\0' in the end of the result and returns it
    result[indexResult] = '\0';
    return result;
}
