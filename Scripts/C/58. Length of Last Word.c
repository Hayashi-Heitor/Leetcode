int lengthOfLastWord(char *s) {
    int index = 0, count = 0;

    while (s[index] != '\0') //get to the end of the string
        index++;
    while (!((s[index] >= 'a' && s[index] <= 'z') || (s[index] >= 'A' && s[index] <= 'Z'))) //goes back until find letters
        index--;
    while (((s[index] >= 'a' && s[index] <= 'z') || (s[index] >= 'A' && s[index] <= 'Z')) && index > 0) { //increases count for each letter while also going back
        index--;
        count++;
    }
    if ((s[index] >= 'a' && s[index] <= 'z') || (s[index] >= 'A' && s[index] <= 'Z')) //check last position
        count++;
    return count;
}
