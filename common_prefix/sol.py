class Solution:
    def longestCommonPrefix(self, v: List[str]) -> str:
        ans=""
        v=sorted(v)
        first=v[0]
        last=v[-1]
        for i in range(min(len(first),len(last))):
            if(first[i]!=last[i]):
                return ans
            ans+=first[i]
        return ans 

test_cases = [
    (["caa","","a","acb"], ""),
    (["ref","flow","flight"], ""),
    (["flower", "flow", "flight"], "fl"),
    (["dog", "racecar", "car"], ""),
    (["ab", "a"], "a"),
    (["", "b"], ""),
    (["a"], "a"),
    (["aa", "aa"], "aa"),
    (["aa", "ab"], "a"),            
    (["aa", "a"], "a"),            
    (["a", "a"], "a"),
]

sol = Solution()

for test_case in test_cases:
    print(f"test_case[0]: {test_case[0]}")
    print(f"test_case[1]: {test_case[1]}")

    if sol.longestCommonPrefix(test_case[0]) != test_case[1]:
        raise # True