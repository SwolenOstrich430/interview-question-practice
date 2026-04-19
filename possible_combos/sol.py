from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.combos = []
        self.set_combos(candidates, target, 0, [])
        
        return self.combos

    def set_combos(
        self,
        candidates: List[int], 
        target: int, 
        curr_sum: int, 
        curr_combos: List[int]
    ) -> None:
        if curr_sum > target:
            return 
        elif curr_sum == target: 
            self.combos.append(curr_combos)

        for i in range(len(candidates)):
            self.set_combos(
                candidates[i:], 
                target, 
                curr_sum + candidates[i], 
                curr_combos + [candidates[i]]
            )

sol = Solution() 

test_cases = [
    ([2,3,6,7], 10, [[2,2,2,2,2],[2,2,3,3],[2,2,6],[3,7]])
]

for test_case in test_cases: 
    print(test_case[0])
    print(test_case[1])
    print(test_case[2])

    if list(sorted(sol.combinationSum(test_case[0], test_case[1]))) != list(sorted(test_case[2])):
        raise