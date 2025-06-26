# Returns the name, population and area from the countries that have a area of at least three million,
# or a population of at least twenty-five million
SELECT name, population, area FROM World
WHERE area >= 3000000 OR population >= 25000000