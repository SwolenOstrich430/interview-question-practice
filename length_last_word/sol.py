class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_strip = s.strip()

        i = len(s_strip) - 1
        count = 0
        
        while i >= 0 and s_strip[i] != " ":
            i -= 1
            count += 1

        return count
    

sol = Solution()

test_cases = [
    ["a", 1]
]

for test_case in test_cases:
    if sol.lengthOfLastWord(test_case[0]) != test_case[1]:
        raise