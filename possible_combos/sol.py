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
        curr_combos: Tuple[int]
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