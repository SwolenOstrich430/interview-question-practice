class Solution:
    def threeSum(self, nums):
        complement_map = {}
        complement = None
        target_num = 0

        for i in range(len(nums)):
            for j in range(len(nums[(i + 1):])):
                complement = target_num - (nums[i] + nums[j + 1 + i])
                if complement not in complement_map:
                    complement_map[complement] = []

                complement_map[complement].append([i, j + 1 + i])

        final_nums = set()
        curr_list = None
        for i in range(len(nums)):
            if nums[i] in complement_map:
                for arr in complement_map[nums[i]]:
                    if i not in arr:
                        curr_list = [nums[i], nums[arr[0]], nums[arr[1]]]
                        curr_list.sort()
                        final_nums.add(tuple(curr_list))

        return list(final_nums)

        
sol = Solution()
sol.threeSum([-1,0,1,2,-1,-4])
