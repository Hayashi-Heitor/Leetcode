bool isHappy(int n) {
    int result;

    // Reduces the number util it is a single-digit
    while(n > 9) {
        result = 0;

        // Sums the square of the last digit on the result and removes the digit from n
        while (n > 9) {
            result += (n % 10) * (n % 10);
            n /= 10;
        }

        result += n * n;
        n = result;
    }

    // Returns true if the final number is 1 or 7 (7 -> 49 ->97 -> 130  ->10 -> 1)
    return(n == 1 || n == 7); 
}