from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(len(nums[i + 1:])):
            if nums[i] + nums[i + j + 1] == target:
                return [i, i + j + 1]
            
print(twoSum([3, 2, 4], 6))