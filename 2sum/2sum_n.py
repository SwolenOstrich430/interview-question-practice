from collections import List 

def twoSum(nums: List[int], target: int) -> List[int]:
    complements = {}

    for i in range(len(nums)):
        complements[nums[i]] = i

    for i in range(len(nums)):
        if ((target - nums[i] in complements) and
            complements[target - nums[i]] != i):
            return [i, complements[target - nums[i]]]

print(twoSum([3, 2, 4], 6))