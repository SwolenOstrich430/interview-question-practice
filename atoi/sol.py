import re 

class Solution:
    def myAtoi(self, s: str) -> int:
        final_str = s.lstrip()
        match = re.match(r'^[\+\-]?\d+', final_str)   
        
        if not match:
            return 0
        
        final_str = match.group(0)
        final_num = int(final_str)

        if final_num < -2**31:
            return -2**31
        elif final_num > 2**31 - 1:
            return 2**31 - 1
        
        return final_num