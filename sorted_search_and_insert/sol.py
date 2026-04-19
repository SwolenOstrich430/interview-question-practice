from typing import List 


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 0 or (len(nums) == 1 and nums[0] == target):
            return 0
        elif len(nums) == 1:
            return 0 if target < nums[0] else 1

        lead = len(nums) - 1
        lag = 0 
        mid = int(lead / 2)
        closest_val, closest_index = nums[mid], mid 

        while lag <= lead: 
            if target == nums[lead]:
                return lead
            elif target == nums[lag]:
                return lag
            elif target == nums[mid]:
                return mid 
            
            if abs(nums[lead] - target) < abs(closest_val - target):
                closest_val = nums[lead]
                closest_index = lead
            if abs(nums[lag] - target) < abs(closest_val - target):
                closest_val = nums[lag]
                closest_index = lag
            if abs(nums[mid] - target) < abs(closest_val - target):
                closest_val = nums[mid]
                closest_index = mid

            if nums[mid] < target:
                lag = mid
                lead -= 1
            else:
                lag += 1
                lead = mid

            mid = int((lag + lead) / 2)
        
        if target > closest_val:
            return closest_index + 1
        else:
            return closest_index

sol = Solution()

test_cases = [
    # ([1,3,5,6], 5, 2),
    # ([1,3,5,6], 2, 1),
    # ([1,3,5,6], 7, 4),
    # ([1,3,5,6], 0, 0),
    ([1], 0, 0),
    ([1], 1, 0),
    ([1], 2, 1)
] 

for test_case in test_cases:
    print(f"test_case[0]: {test_case[0]}")
    print(f"test_case[1]: {test_case[1]}")
    print(f"sol.searchInsert(test_case[0], test_case[1]): {sol.searchInsert(test_case[0], test_case[1])}")

    if sol.searchInsert(test_case[0], test_case[1]) != test_case[2]:
        raise # True