from typing import List

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if 1 in [m, n]:
            return 1
        elif 0 in [m, n]:
            return 0
            
        self.total_paths = 0
        self.paths_helper(m, n, 0, 0, {})
        return self.total_paths

    def paths_helper(self, y: int, x: int, y_idx: int, x_idx: int, mem: dict) -> int:
        if y_idx == y - 1 and x_idx == x - 1:
            return 1
        elif (y_idx < 0 or y_idx >= y) or (x_idx < 0 or x_idx >= x):
            return 0

        if (y_idx, x_idx) in mem:
            return mem[(y_idx, x_idx)]

        mem[(y_idx, x_idx)] = (
            self.paths_helper(y, x, y_idx + 1, x_idx, mem) + 
            self.paths_helper(y, x, y_idx, x_idx + 1, mem) 
        )
        self.total_paths = mem[(y_idx, x_idx)]

        return self.total_paths
