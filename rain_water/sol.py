from typing import List 

class Solution:
    def trap(self, height: List[int]) -> int:
        nums = height
        '''
            for two non-consecutive indexes: 
                - find the width (distance apart)
                - the minimum height
                - and any filled space between those two non-consecutive indexes 

            for i in range(len(heights)): 
                skip until height > 0
                store that height in variable, start_height
                if height[i] <= height[i + 1] don't set start_height
                if height[i] > height[i + 1]:
                    - continue until height[i...] >= start_height
                    - until that happens
                        - keep track of what fill space there is 
                        - fill space: 
                            - min(start_height, start_height - height[i])
                        - add each fill space to a running total
                if we get to height[i...] >= start_height or i = len(nums) - 1
                    - add current total to the running total
        '''
        total_fill = 0
        curr_range_fill = 0
        next_highest_idx = None 
        start_range_idx = None
        i = 0

        while i < len(nums):
            if start_range_idx is not None and i > start_range_idx + 1 and \
                (i == len(nums) - 1 or nums[i] != nums[i - 1]):
                if next_highest_idx is None or nums[next_highest_idx] < nums[i]:
                    next_highest_idx = i
                
            if start_range_idx is not None and nums[start_range_idx] <= nums[i] and start_range_idx + 1 != i:
                total_fill += curr_range_fill
                start_range_idx = None 
                next_highest_idx = None
                curr_range_fill = 0 
            elif i == len(nums) - 1 and start_range_idx is not None and next_highest_idx is not None: 
                less_than_next_highest = list(filter(
                    lambda num: num < nums[next_highest_idx], 
                    nums[start_range_idx + 1:next_highest_idx]
                ))
                 
                if len(less_than_next_highest) != 0:
                    curr_range_fill = nums[next_highest_idx] * len(less_than_next_highest)
                    curr_range_fill -= sum(less_than_next_highest)
                    total_fill += curr_range_fill
                
                curr_range_fill = 0
                i = next_highest_idx
                start_range_idx = None
                next_highest_idx = None
                continue 

            if start_range_idx is None:
                if i < len(nums) - 1 and nums[i] > 0 and nums[i] > nums[i + 1]:
                    start_range_idx = i
                    curr_range_fill = 0
            else:
                curr_range_fill += nums[start_range_idx] - nums[i]
            
            i += 1

        return total_fill


sol = Solution()

test_cases = [
    [[0,2,5,0,6,9,8,7,4,4,5,6], 10],
    [[2,4,5,6,8,5,5,0,0,0,3,3], 9],
    [[9,6,8,8,5,6,3], 3],
    [[0,7,1,4,6], 7],
    [[5, 4, 1, 2], 1],
    [[4, 2, 3], 1],
    [[0,1,0,2,1,0,1,3,2,1,2,1], 6]
]

for test_case in test_cases:
    print(test_case[0])
    print(test_case[1])

    if sol.trap(test_case[0]) != test_case[1]:
        raise 