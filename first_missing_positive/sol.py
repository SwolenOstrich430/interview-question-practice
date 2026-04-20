from typing import List 

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 1

        nums = sorted(list(set(filter(lambda num: num > 0, nums))))

        if len(nums) == 0:
            return 1

        last_num = nums[0]

        if last_num != 1:
            return 1

        for i in range(1, len(nums)): 
            if last_num + 1 != nums[i]:
                break

            last_num = nums[i]

        return last_num + 1
        
        

sol = Solution()
test_cases = [
    [[1,2,0], 3]
]

for test_case in test_cases: 
    print(test_case[0])
    print(test_case[1])

    if sol.firstMissingPositive(test_case[0]) != test_case[1]:
        raise 