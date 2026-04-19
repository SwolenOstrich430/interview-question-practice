class Solution:
    def longestValidParentheses(self, s: str) -> int:
        curr_max = 0
        curr_range = 0
        pending_completes = []
        complete_ranges = []
        char = None 

        for i in range(len(s)):
            char = s[i]

            if char == ")" and len(pending_completes) <= 0:
                curr_range = 0
            elif char == ")":
                complete_ranges += [pending_completes.pop(), i]
            elif char == "(":
                pending_completes.append(i)

        curr_index = 0
        complete_ranges.sort()
        while curr_index < len(complete_ranges) - 1:

            if curr_range > 0 and complete_ranges[curr_index] - 1 != complete_ranges[curr_index - 1]:
                curr_range = 0

            if complete_ranges[curr_index] + 1 == complete_ranges[curr_index + 1]:
                curr_range += 2
                curr_index += 2
            else:
                curr_range = 0
                curr_index += 1

            if curr_max < curr_range:
                curr_max = curr_range

        return curr_max

          
            

            

sol = Solution()

test_cases = [\
    (")()())", 4),
    ("()(()", 2),
    ("(()", 2),
    (")()())", 4),
    ("", 0)
]

for test_case in test_cases:
    print(f"test_case[0]: {test_case[0]}")
    print(f"test_case[1]: {test_case[1]}")
    print(f"sol.longestValidParentheses(test_case[0]): {sol.longestValidParentheses(test_case[0])}")

    if sol.longestValidParentheses(test_case[0]) != test_case[1]:
        raise # True    
