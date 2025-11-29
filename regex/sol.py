class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        str_idx = 0
        reg_idx = 0

        while str_idx < len(s):
            if reg_idx >= len(p):
                return False
            elif not self.is_special_char(reg_idx, p) and s[str_idx] == p[reg_idx]:
                str_idx += 1
            elif not self.is_special_char(reg_idx, p) and s[str_idx] != p[reg_idx]:
                return False
            elif self.is_plain_wildcard_char(reg_idx, p):
                str_idx += 1
            elif self.is_look_behind_char(reg_idx, p):
                str_idx = self.advance_index_for_look_behind_char(
                    reg_idx, p, str_idx, s
                )

                if str_idx == -1:
                    return False

            reg_idx += 1
                
        return True

    def advance_index_for_look_behind_char(self, reg_idx, p, str_idx, s):
        assert self.is_look_behind_char(reg_idx, p)
        assert reg_idx != 0

        if self.is_look_behind_char(reg_idx - 1, p):
            return str_idx

        if not self.is_special_char(reg_idx - 1, p):
            while str_idx < len(s) and p[reg_idx - 1] == s[str_idx]:
                str_idx += 1
        elif self.is_wildcard_char(reg_idx - 1, p) and reg_idx == len(p) - 1:
            str_idx = len(s)
        elif self.is_wildcard_char(reg_idx - 1, p):
            future_idx = s[str_idx:].find(p[reg_idx + 1])

            if future_idx == -1:
                str_idx = future_idx
            else:
                str_idx += future_idx

        return str_idx
            
    def is_plain_wildcard_char(self, reg_idx, p):
        if reg_idx == len(p) - 1:
            return self.is_wildcard_char(reg_idx, p)
        else:
            return self.is_wildcard_char(reg_idx, p) and \
                not self.is_look_behind_char(reg_idx + 1, p)

    def is_special_char(self, i, p):
        return False if i >= len(p) else self.is_wildcard_char(i, p) or self.is_look_behind_char(i, p)

    def is_wildcard_char(self, i, p):
        return False if i >= len(p) else p[i] == '.'

    def is_look_behind_char(self, i, p):
        return False if i >= len(p) else p[i] == '*'


sol = Solution()
assert not sol.isMatch("aa", "a")
assert sol.isMatch("aa", "aa")
assert sol.isMatch("aa", "a*")
assert sol.isMatch("aa", ".*")
assert sol.isMatch("aa", "a.*")
assert not sol.isMatch("aa", "a.*b")
assert sol.isMatch("aab", "a.*b")
