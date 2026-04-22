from typing import List

class Solution:
    def paths(self, m: int, n: int) -> int:
        self.route = []
        self.paths_helper(m, n, 0, 0, [], {})
        return len(self.route)

    def paths_helper(self, y: int, x: int, y_idx: int, x_idx: int, path, mem: List[List[int]]) -> int:
        if y_idx == y - 1 and x_idx == x - 1:
            if path not in self.route: 
                self.route.append(path)
                
            return 
        elif (y_idx < 0 or y_idx >= y) or (x_idx < 0 or x_idx >= x):
            return

        if x_idx < x - 1 and (y_idx, x_idx + 1) not in path:
            mem[(y_idx, x_idx + 1)] = True 
            self.paths_helper(y, x, y_idx, x_idx + 1, path + [(y_idx, x_idx + 1)], mem)

        if y_idx < y - 1 and (y_idx + 1, x_idx) not in path:
            mem[(y_idx + 1, x_idx)] = True
            self.paths_helper(y, x, y_idx + 1, x_idx, path + [(y_idx + 1, x_idx)], mem)




sol = Solution()

test_cases = [
    [3, 2, 3],
    [3, 7, 28]
]

for test_case in test_cases:
    if sol.paths(test_case[0], test_case[1]) != test_case[2]:
        raise 