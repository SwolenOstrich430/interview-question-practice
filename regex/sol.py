class Solution:
    '''
        . = free space 
        * = 0+ of the i-1
        + = 1+ of the i-1
    '''
    def isMatch(self, s: str, p: str) -> bool:
        return self._is_match_helper(s, 0, p, 0)

    def _is_match_helper(self, s, s_idx, p, p_idx):
        if p_idx >= len(p):
            return s_idx >= len(s)
        
        curr_char = s_idx < len(s) and s[s_idx]
        _is_match = p[p_idx] in [curr_char, "."]

        if p_idx + 1 < len(p) and p[p_idx + 1] == "+":
            if not _is_match and s[s_idx - 1] == p[p_idx]:
                return self._is_match_helper(s, s_idx, p, p_idx + 2)
            elif _is_match and s_idx >= len(s) - 1:
                return self._is_match_helper(s, s_idx + 1, p, p_idx + 2)
            
            return _is_match and (
                self._is_match_helper(s, s_idx + 1, p, p_idx) or 
                self._is_match_helper(s, s_idx + 1, p, p_idx + 1) 
            )
        elif p_idx + 1 < len(p) and p[p_idx + 1] == "*":
            if s_idx >= len(s):
                return self._is_match_helper(s, s_idx, p, p_idx + 2)
            else:
                return (
                    self._is_match_helper(s, s_idx, p, p_idx + 2) or
                    (_is_match and self._is_match_helper(s, s_idx + 1, p, p_idx))
                )
        else:
            return _is_match and self._is_match_helper(s, s_idx + 1, p, p_idx + 1)


sol = Solution()
if not sol.isMatch("abb", "ab+"):
    raise # True
if not sol.isMatch("aaaaaab", "a+b"):
    raise # True
if not sol.isMatch("aaaaaab", "a+b+"):
    raise # True
if not sol.isMatch("ab", "a+b+"):
    raise # True
if sol.isMatch("b", "a+b+"):
    raise # True
if sol.isMatch("a", "ab+"):
    raise # True
if not sol.isMatch("ab", "ab+c*"):
    raise # True
if not sol.isMatch("abbbbbb", "ab+c*"):
    raise # True
if sol.isMatch("aaaaaaaaaaaaaaaaaaa", "a*a*a*a*a*a*a*a*a*b"):
    raise # Fakse
if not sol.isMatch("abcaaaaaaabaabcabac", ".*b*b*"):
    raise # True
if not sol.isMatch("ab", ".*.."):
    raise # True
if not sol.isMatch("bbbba", ".*a*a"):
    raise # True
if sol.isMatch("aaa", "aaaa"):
    raise # False
if not sol.isMatch("a", "ab*"):
    raise # True
if not sol.isMatch("aaa", "ab*ac*a"): # True
    raise Exception("Expected True")
if not sol.isMatch("aaa", "ab*a*c*a"): # True
    raise Exception("Expected True")
if sol.isMatch("aaa", "ab*a"): # False
    raise Exception("Expected False")
if sol.isMatch("ab", ".*c"):
    raise Exception("Expected False")
if sol.isMatch("mississippi", "mis*is*p*."):
    raise Exception("Expected False")