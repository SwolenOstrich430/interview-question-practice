class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.match_helper(0, p, 0, s)

    def match_helper(self, reg_idx, p, str_idx, s):
        if reg_idx == len(p) and str_idx == len(s):
            return True

        if reg_idx >= len(p):
            return False
            
        curr_reg_char = p[reg_idx]
        is_lookbehind_star = reg_idx > 0 and p[reg_idx - 1] == "*"

        if is_lookbehind_star:
            # try with 0 matches 
            if self.match_helper(reg_idx + 1, p, str_idx, s):
                return True
            # try with 1+ matches         
            while str_idx < len(s) and (s[str_idx] == p[reg_idx - 1] or p[reg_idx - 1] == "."):
                if self.match_helper(reg_idx + 1, p, str_idx + 1, s):
                    return True 

                str_idx += 1

            return False
        else:
            if p[reg_idx] == "." or s[str_idx] == p[reg_idx]:
                return self.match_helper(reg_idx + 1, p, str_idx + 1, s)
            elif str_idx < len(s) - 1 and reg_idx + 1 < len(p) and p[reg_idx + 1] == "*":
                return self.match_helper(reg_idx + 1, p, str_idx, s)

            return False

sol = Solution()
# assert not sol.isMatch("mississippi", "mis*is*p*.")
# assert sol.isMatch("aaa", "a*a")
# assert sol.isMatch("aaa", "aaaa")
assert not sol.isMatch("ab", ".*c")
assert sol.isMatch("aab", "c*a*b")
assert not sol.isMatch("aa", "a")
assert sol.isMatch("aa", "aa")
assert sol.isMatch("aa", "a*")
assert sol.isMatch("aa", ".*")
assert sol.isMatch("aa", "a.*")
assert not sol.isMatch("aa", "a.*b")
assert sol.isMatch("aab", "a.*b")
