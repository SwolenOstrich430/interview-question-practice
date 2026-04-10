from typing import List


class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        horizontal_sums_by_index = {}
        vertical_sums_by_index = {}

        for y in range(len(grid)):
            if y not in horizontal_sums_by_index: 
                horizontal_sums_by_index[y] = 0

            for x in range(len(grid[y])): 
                if sum(grid[0][0:x+1]) == sum(grid[0][x+1:-1]): 
                    return True 
                
                horizontal_sums_by_index[y] += grid[y][x]

                if x not in vertical_sums_by_index: 
                    vertical_sums_by_index[x] = 0  

                if (sum(vertical_sums_by_index.values()) ) == grid[y][x]:
                    return True 
                
                vertical_sums_by_index[x] += grid[y][x]

        return (
            (len(vertical_sums_by_index.values()) > 1 and len(set(vertical_sums_by_index.values())) == 1) or
            (len(horizontal_sums_by_index.values()) > 1 and len(set(horizontal_sums_by_index.values())) == 1)
        )

            

sol = Solution()
print(sol.canPartitionGrid([[1, 2], [3, 4]])) # True
print(sol.canPartitionGrid([[1, 1], [1, 1]])) # True
print(sol.canPartitionGrid([[1, 2], [3, 4], [5, 6]])) # False   
print(sol.canPartitionGrid([[28443],[33959]])) # True
print(sol.canPartitionGrid([[42047],[57775],[99822]]))
print(sol.canPartitionGrid([[65917,79299]]))
print(sol.canPartitionGrid([[42047],[57775],[99822]])) # False
