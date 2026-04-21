from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = None
        curr_max = sum(nums)

        for num in nums:
            if curr_sum is not None:
                curr_sum += num
            else:
                curr_sum = num
            
            if num > curr_max: 
                curr_max = num 

            if curr_sum < 0:
                curr_sum = 0
            else:
                curr_max = max(curr_max, curr_sum)

        return curr_max


sol = Solution()

test_cases = [
    [[2,-1,3,-1], 4],
    [[-1,1,2,1], 4],
    [[2,-1,1,1], 3],
    [[1,2,-1,-2,2,1,-2,1], 3],
    [[-1, -2], -1],
    [[-2, -1], -1],
    [[-2,1,-3,4,-1,2,1,-5,4], 6]
]

for test_case in test_cases:
    if sol.maxSubArray(test_case[0]) != test_case[1]:
        raise