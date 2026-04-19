from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        elif len(nums) == 1:
            return 0 if nums[0] == target else -1
        
        curr_index = int(len(nums) / 2)
        leading_index = len(nums) - 1
        lagging_index = 0
        
        while lagging_index < leading_index:
            if nums[lagging_index] == target:
                return lagging_index
            elif nums[leading_index] == target:
                return leading_index
    
            lagging_index += 1 
            leading_index -= 1

            if nums[curr_index] == target:
                return curr_index 
            elif nums[curr_index] < target:
                curr_index = int((curr_index + lagging_index) / 2)
            elif nums[curr_index] > target:
                curr_index = int((curr_index + leading_index) / 2)
        
            if nums[curr_index] == target:
                return curr_index
        
        return -1
            

sol = Solution()

test_cases = [
    ([4,5,6,7,0,1,2], 5, 1),
    ([4,5,6,7,0,1,2], 1, 5),
    ([5,1,3], 0, -1),
    ([5,1,2,3,4], 1, 1),
    ([5,1,2,3,4], 5, 0),
    ([5,1,2,3,4], 3, 3),
    ([1, 3], 0, -1),
    ([4,5,6,7,0,1,2], 3, -1),
    ([4,5,6,7,0,1,2], 0, 4),
    ([1], 0, -1)
]       

for test_case in test_cases:
    print(f"test_case[0]: {test_case[0]}")
    print(f"test_case[1]: {test_case[1]}")
    print(f"sol.search(test_case[0], test_case[1]): {sol.search(test_case[0], test_case[1])}")

    if sol.search(test_case[0], test_case[1]) != test_case[2]:
        raise # True
