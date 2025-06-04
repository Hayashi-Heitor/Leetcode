int largestAltitude(int* gain, int gainSize) {
    int highestAltitude = 0;
    int currentAltitude = 0;

    // Checks all the gainSizes
    for(int index = 0; index < gainSize; index++) {
        currentAltitude += gain[index];

        // If the current is highest than the highest we make it the new highest
        if(currentAltitude > highestAltitude)
            highestAltitude = currentAltitude;
    }

    return highestAltitude;
}