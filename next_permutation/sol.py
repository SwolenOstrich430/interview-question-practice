from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        if len(nums) <= 1:
            return

        attempts_remaining = True 
        curr_index = len(nums) - 1 

        while attempts_remaining:
            if nums[curr_index] > nums[curr_index - 1]:
                temp = sorted(nums[curr_index - 1:])
                next_index = temp.index(nums[curr_index - 1]) + 1

                while next_index < len(temp) and temp[next_index] == temp[next_index - 1]:
                    next_index += 1

                nums[curr_index - 1] = temp[next_index]
                temp.pop(next_index)
                nums[curr_index:] = temp
                break 
           
            curr_index -= 1
            if curr_index == 0:
                nums.sort()
                attempts_remaining = False

                
sol = Solution()

test_cases = [
    ([1,5,1], [5,1,1]),
    ([1,2,3], [1,3,2]),
    ([3,2,1], [1,2,3]),
    ([1,1,5], [1,5,1])
]

for test_case in test_cases:
    print(f"test_case[0]: {test_case[0]}")
    print(f"test_case[1]: {test_case[1]}")
    
    sol.nextPermutation(test_case[0])

    if test_case[0] != test_case[1]:
        raise # True