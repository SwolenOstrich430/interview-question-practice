from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
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
        if len(set(candidates)) == 1:
            if candidates[0] * len(candidates) + curr_sum == target:
                curr_combos += [candidates[0]] * len(candidates)
                curr_sum += candidates[0] * len(candidates)
                
        if curr_sum > target:
            return 
        elif curr_sum == target: 
            if sorted(curr_combos) not in self.combos:
                self.combos.append(sorted(curr_combos))

            return 

        for i in range(len(candidates)):
            self.set_combos(
                candidates[:i] + candidates[i+1:], 
                target, 
                curr_sum + candidates[i], 
                curr_combos + [candidates[i]]
            )

sol = Solution() 

test_cases = [
    # ([1], 1, [[1]]),
    ([1, 1], 2, [[1, 1]])
]

for test_case in test_cases: 
    print(test_case[0])
    print(test_case[1])
    print(test_case[2])

    if list(sorted(sol.combinationSum2(test_case[0], test_case[1]))) != list(sorted(test_case[2])):
        raise