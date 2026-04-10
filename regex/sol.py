class Solution:
    '''
        . = free space 
        * = 0+ of the i-1
    '''
    def isMatch(self, s: str, p: str) -> bool:
        return self._is_match_helper(s, 0, p, 0)

    def _is_match_helper(self, s, s_idx, p, p_idx):
        if p_idx >= len(p):
            return s_idx >= len(s)
        elif s_idx >= len(s):
            return (
                p_idx >= len(p) or (
                    p_idx + 1 < len(p) 
                    and p[p_idx + 1] == "*" 
                    and self._is_match_helper(s, s_idx, p, p_idx + 2)
                )
            )

        if p_idx + 1 < len(p) and p[p_idx + 1] == "*":
            return (
                self._is_match_helper(s, s_idx, p, p_idx + 2) or
                (p[p_idx] in [s[s_idx], "."] and self._is_match_helper(s, s_idx + 1, p, p_idx))
            )
        else:
            return p[p_idx] in [s[s_idx], "."] and self._is_match_helper(s, s_idx + 1, p, p_idx + 1)
