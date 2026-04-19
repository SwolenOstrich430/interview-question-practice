from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        elif len(nums) == 1:
            return [-1, -1] if nums[0] != target else [0, 0]
            
        lagging = 0 
        leading = len(nums)
        curr_index = int(leading / 2)

        while lagging < leading and nums[curr_index] != target:
            if lagging >= 0 and nums[lagging] == target:
                curr_index = lagging 
                break 
            elif leading < len(nums) and nums[leading] == target:
                curr_index = leading 
                break 

            leading -= 1
            lagging += 1
            curr_index = int((lagging + leading) / 2)

        start_fin_indexes = [None, None]

        if curr_index < len(nums) - 1 and nums[curr_index + 1] == target:
            leading = curr_index + 1
            lagging = curr_index
        elif curr_index > 0 and nums[curr_index - 1] == target: 
            lagging = curr_index - 1 
            leading = curr_index
        elif nums[curr_index] == target:
            return [curr_index, curr_index]
        else:
            return [-1, -1]

        while (lagging >= 0 and nums[lagging] == target) or (leading < len(nums) and nums[leading] == target):
            if lagging >= 0 and nums[lagging] != target and nums[0] == None:
                start_fin_indexes[0] = nums[lagging + 1]
            elif lagging >= 0 and nums[lagging] == target:
                start_fin_indexes[0] = lagging
                lagging -= 1
                

            if leading < len(nums) and nums[leading] != target and nums[1] == None:
                start_fin_indexes[1] = nums[leading - 1]
            elif leading < len(nums) and nums[leading] == target:
                start_fin_indexes[1] = leading
                leading += 1

        return start_fin_indexes


sol = Solution()

test_cases = [
    ([5,7,7,8,8,10], 8, [3, 4]),
    ([5,7,7,8,8,10], 6, [-1, -1]),
    ([5,7,7,8,8,10], 5, [0, 0]),
    ([5,7,7,8,8,10], 10, [5, 5]),
    ([1], 1, [0, 0]),
    ([1], 0, [-1, -1])
]

for test_case in test_cases:
    print(f"test_case[0]: {test_case[0]}")
    print(f"test_case[1]: {test_case[1]}")
    print(f"test_case[2]: {test_case[2]}")
    print(f"sol.searchRange(test_case[0], test_case[1]): {sol.searchRange(test_case[0], test_case[1])}")

    if sol.searchRange(test_case[0], test_case[1]) != test_case[2]:
        raise # True