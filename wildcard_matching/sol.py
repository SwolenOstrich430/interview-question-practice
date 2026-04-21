class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # if is ? s_i++ p_i++
        # if is literal and s[s_i] == p[p_i] s_i++ p_i++
        # if is literal and s[s_i] != p[p_i] but we've previously had an asterisk
        #   reset p_i to the last asterisk_i + 1
        #   s_i++ 
        # else 
        #   false  
        # return p_idx == len(p) or (len(set(p[p_idx:])) == 1 and p[p_idx] == "*")
        last_ast_idx = None 
        last_s_idx_for_ast = None
        s_idx = 0 
        p_idx = 0 

        while s_idx < len(s):
            if p_idx < len(p) and p[p_idx] == "*":
                last_s_idx_for_ast = s_idx
                last_ast_idx = p_idx
                p_idx += 1
            elif p_idx < len(p) and (p[p_idx] == "?" or p[p_idx] == s[s_idx]):
                p_idx += 1
                s_idx += 1
            elif last_ast_idx is not None:
                last_s_idx_for_ast += 1
                s_idx = last_s_idx_for_ast
                p_idx = last_ast_idx + 1
            else: 
                return False 

        return p_idx >= len(p) or (len(set(p[p_idx:])) == 1 and p[p_idx] == "*")