int lengthOfLastWord(char *s) {
    int index = 0, count = 0;

    while (s[index] != '\0')
        index++;
    while (!((s[index] >= 'a' && s[index] <= 'z') || (s[index] >= 'A' && s[index] <= 'Z')))
        index--;
    while (((s[index] >= 'a' && s[index] <= 'z') || (s[index] >= 'A' && s[index] <= 'Z')) && index > 0) {
        index--;
        count++;
    }
    if ((s[index] >= 'a' && s[index] <= 'z') || (s[index] >= 'A' && s[index] <= 'Z'))
        count++;
    return count;
}
