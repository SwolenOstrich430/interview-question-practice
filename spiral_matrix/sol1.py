from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        nums = matrix
        vals = []
        mem = {}
        y = 0
        x = 0
        y_lock = True
        y_dir = -1
        x_dir = 1

        while len(vals) < len(matrix) * len(matrix[0]):
            vals.append(matrix[y][x])

            if (
                y_lock and 
                (x + x_dir in [len(matrix), -1] or 
                (y, x + x_dir) in mem)
            ):
                y_dir *= -1
                y_lock = not y_lock
            elif (
                not y_lock and 
                (y + y_dir in [len(matrix[0]), -1] or 
                (y + y_dir, x) in mem)
            ):
                x_dir *= -1
                y = max(y, 0)
                y_lock = not y_lock
            
            mem[(y, x)] = True

            if not y_lock:
                y += y_dir
            else:
                x += x_dir
        
        return vals
    

sol = Solution()

test_cases = [
    [[[1,2,3],[4,5,6],[7,8,9]], [1,2,3,4,5,6,7,8,9]]
]

for test_case in test_cases:
    if sol.spiralOrder(test_case[0]) != test_case[1]:
        raise