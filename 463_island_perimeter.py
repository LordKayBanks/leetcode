# 463. Island Perimeter

# You are given a map in form of a two-dimensional integer grid 
# where 1 represents land and 0 represents water. 
# Grid cells are connected horizontally/vertically (not diagonally). 
# The grid is completely surrounded by water, and there is exactly one island 
# (i.e., one or more connected land cells). The island doesn't have "lakes" 
# (water inside that isn't connected to the water around the island). 
# One cell is a square with side length 1. 
# The grid is rectangular, width and height don't exceed 100. 
# Determine the perimeter of the island.

# Example:

# [[0,1,0,0],
#  [1,1,1,0],
#  [0,1,0,0],
#  [1,1,0,0]]

# Answer: 16
# Explanation: The perimeter is the 16 yellow stripes in the image below:

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        https://leetcode.com/problems/island-perimeter/discuss/95001/clear-and-easy-java-solution

        1. loop over the matrix and count the number of islands;
        2. if the current dot is an island, count if it has any right neighbour or down neighbour;
        3. the result is islands * 4 - neighbours * 2
        """
        islands = 0
        neighbours = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    islands += 1
                    if i < len(grid)-1 and grid[i+1][j] == 1:
                        neighbours += 1
                    if j < len(grid[0])-1 and grid[i][j+1] == 1:
                        neighbours += 1
        return islands * 4 - neighbours * 2

s = Solution()
grid = [[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]
print(s.islandPerimeter(grid))
        