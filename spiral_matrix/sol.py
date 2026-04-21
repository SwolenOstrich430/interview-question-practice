from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # [1,2,3,4]
        # [5,6,7,8]
        # [9,10,11,12]
        # [13,14,15,16]

        # start direction => i is locked, j to positive 
        # then => j is locked and i to negative
        # then => i is locked, j to positive 
        grid = [[0 for _ in range(n)] for _ in range(n)]
        x_dir = 1
        y_dir = -1
        y_idx = 0
        x_idx = 0
        y_locked = True

        for i in range(1, n**2 + 1):
            if (y_locked and x_idx >= n) or (not y_locked and y_idx >= n) or \
                (y_locked and x_idx < 0) or (not y_locked and y_idx < 0) or \
                grid[y_idx][x_idx] != 0:
                y_locked = not y_locked

                if not y_locked:
                    y_dir *= -1
                    x_idx -= x_dir
                    y_idx += y_dir
                else:
                    x_dir *= -1
                    x_idx += x_dir
                    y_idx -= y_dir


            if y_locked:
                grid[y_idx][x_idx] = i
                x_idx += x_dir
            else:
                grid[y_idx][x_idx] = i
                y_idx += y_dir

        return grid


sol = Solution()

test_cases = [
    [3, [[1,2,3],[8,9,4],[7,6,5]]]
]

for test_case in test_cases:
    if sol.generateMatrix(test_case[0]) != test_case[1]:
        raise