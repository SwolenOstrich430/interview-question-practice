import itertools

class Solution:
    def threeSum(self, nums):
        three_sums = set()
        complement_map = {}

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j]) * -1 not in complement_map:
                    complement_map[(nums[i] + nums[j]) * -1] = [[nums[i], nums[j]]]

                if [nums[i], nums[j]] not in complement_map[(nums[i] + nums[j]) * -1]:
                    complement_map[(nums[i] + nums[j]) * -1].append([nums[i], nums[j]])

        for complement, curr_vals in complement_map.items():
            for curr_val in curr_vals:
                if complement in nums and (complement not in curr_val or nums.count(complement) > curr_val.count(complement)):
                    three_sums.add(tuple(sorted(curr_val + [complement])))


        return list(three_sums)

test_cases = [
    ([2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10], [[-10,5,5],[-5,0,5],[-4,2,2],[-3,-2,5],[-3,1,2],[-2,0,2]]),
    ([-1,0,1,0], [[-1,0,1]]),
    ([-100,-70,-60,110,120,130,160], [[-100,-60,160],[-70,-60,130]]),
    ([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]),
    ([0,1,1], []),
    ([0,0,0], [[0,0,0]]),
]

sol = Solution()
for test_case in test_cases:
    print(f"test_case[0]: {test_case[0]}")
    print(f"test_case[1]: {test_case[1]}")

    if sol.threeSum(test_case[0]) != test_case[1]:
        raise # True