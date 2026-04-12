from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(list(filter(lambda num: num is not None, set(nums))))
        return len(nums)



sol = Solution()

test_cases = [
    ([1,1,2], 2),
    ([0,0,1,1,1,2,2,3,3,4], 5)
]

for test_case in test_cases:
    print(f"test_case[0]: {test_case[0]}")
    print(f"test_case[1]: {test_case[1]}")
    print(f"sol.removeDuplicates(test_case[0]): {sol.removeDuplicates(test_case[0])}")

    if sol.removeDuplicates(test_case[0]) != test_case[1]:
        raise # True