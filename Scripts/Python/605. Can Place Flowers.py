class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        plot = 0

        # While there are still plots and flowers to plant continue
        while plot < len(flowerbed) and n > 0:

            # If the plot already has a flower go foward 2 times
            if flowerbed[plot] == 1:
                plot += 1
            
            # If the current plot and its surroundings are 0 plant the flower and advance 2 times
            elif flowerbed[plot] == 0 and (plot == 0 or flowerbed[plot - 1] == 0) and (plot == len(flowerbed) - 1 or flowerbed[plot + 1] == 0):
                flowerbed[plot] = 1
                n -= 1
                plot += 2

            else:
                plot += 1
        
        # If all the flowers were planted return 0
        return n == 0
