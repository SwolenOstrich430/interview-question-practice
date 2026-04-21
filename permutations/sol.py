from typing import List 

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.permutations = []
        self.permute_helper(nums, [])
        return self.permutations

    def permute_helper(self, nums: List[int], curr_permut: List[int]):
        if len(nums) == 1:
            curr_permut.append(nums[0])
            self.permutations.append(curr_permut)
            return

        for i in range(0, len(nums)):
            self.permute_helper(
                nums[:i] + nums[i + 1:], 
                curr_permut + [nums[i]]
            )


            
sol = Solution() 

test_cases = [
    [[1,2,3], [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]]
]

for test_case in test_cases:
    print(test_case[0])
    print(test_case[1])

    if sorted(sol.permute(test_case[0])) != sorted(test_case[1]):
        raise 