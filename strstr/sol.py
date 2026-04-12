class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n_size = len(needle)
        i = 0 

        while (len(haystack) - i) >= n_size:
            if needle == haystack[i:i+n_size]:
                return i 

            i += 1

        return -1
        
sol = Solution()

test_cases = [
    (("hello", "ll"), 2),
    (("aaaaa", "bba"), -1),
    (("", ""), 0),
    (("a", "a"), 0),
    (("mississippi", "issip"), 4)
]

for test_case in test_cases:
    print(f"test_case[0]: {test_case[0]}")
    print(f"test_case[1]: {test_case[1]}")
    print(f"sol.strStr(test_case[0][0], test_case[0][1]): {sol.strStr(test_case[0][0], test_case[0][1])}")

    if sol.strStr(test_case[0][0], test_case[0][1]) != test_case[1]:
        raise # True