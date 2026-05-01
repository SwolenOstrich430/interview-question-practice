class Solution:
    def jump(self, nums):
        num_jumps = 0 
        curr_idx = 0 
        default_jumps = 0
        i = 0 

        while i < len(nums) - 1 and curr_idx < len(nums) - 1:
            
            if (curr_idx + nums[curr_idx] <= i + nums[i] and nums[i + nums[i]] != 0) or \
                ((i + nums[i] == len(nums) - 1) or (i + nums[i] >= len(nums) and nums[i + nums[i]] != 0)):
                num_jumps += default_jumps + 1
                curr_idx = curr_idx + nums[i] 
                default_jumps = 0
            elif (curr_idx == 0 and default_jumps == 0) or (curr_idx != 0 and i >= curr_idx + nums[curr_idx]):
                default_jumps += 1

            i += 1

        return num_jumps
    
sol = Solution() 

test_cases = [
    [[2,0,8,0,3,4,7,5,6,1,0,0,5,9,7,5,3,6], 4],
    [[2,1], 1],
    [[2,3,0,1,4], 2],
    [[5,9,3,2,1,0,2,3,3,1,0,0], 3],
    [[7,0,9,6,9,6,1,7,9,0,1,2,9,0,3], 2],
    [[2,3,1,1,4], 2]
]

for test_case in test_cases:
    if sol.jump(test_case[0]) != test_case[1]:
        raise 