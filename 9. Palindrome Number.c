bool isPalindrome(int x) {
    double original = x, reverse = 0;;

    while (x > 0) {
        reverse = reverse * 10 + (x % 10); //add the last digit to the reverse
        x /= 10; //takes the last digit off the main number
    }
    if (reverse == original)
        return true;
    return false;
}
