import re

class Solution:
    def isNumber(self, s: str) -> bool:
        s_idx = 0 
        in_number = False 
        after_e = False 
        after_decimal = False

        while s_idx < len(s):
            if re.match("[0-9]", s[s_idx]):
                in_number = True 
            elif s[s_idx] == "." and not after_decimal and not after_e:
                after_decimal = True
            elif s[s_idx] == "." and (after_decimal or after_e):
                return False
            elif s[s_idx] in ["e", "E"] and after_e:
                return False

            if after_e and not (re.match("[\.\+\-]", s[s_idx]) or in_number):
                return False

            if s[s_idx] in ["+", "-"] and not (s_idx == 0 or s[s_idx - 1] in ["e", "E"]):
                return False 
            elif s[s_idx] in ["e", "E"]:
                if not in_number:
                    return False 

                after_e = True
                in_number = False
            elif not re.match("[0-9\.\+\-]", s[s_idx]):
                return False 
            elif s_idx > 0 and re.match("[\.\+\-eE]", s[s_idx - 1]) and s[s_idx - 1] == s[s_idx]:
                return False

            s_idx += 1

        return in_number
    
    
    

sol = Solution()

test_cases = [
    ["6e6.5", False],
    [".1.", False],
    ["11", True],
    ["..2", False],
    ["-1E+3", True],
    [".", False],
    ["0", True]
]
        
for test_case in test_cases:
    if sol.isNumber(test_case[0]) != test_case[1]:
        raise