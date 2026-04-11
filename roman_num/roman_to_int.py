NUMERAL_TO_INT_MAP = {
    "i": 1,
    "v": 5,
    "x": 10,
    "l": 50,
    "c": 100,
    "d": 500,
    "m": 1000
}

class Solution:

    def romanToInt(self, s: str) -> int:
        if s is None or len(s) > 16:
            raise ":9"

        s_idx = 0
        prev_val = 0
        total = 0
        curr_char = None

        while s_idx < len(s):
            curr_char = s[-s_idx - 1].lower()

            if curr_char not in NUMERAL_TO_INT_MAP:
                raise f"Bad State: \n\ts: {s} | s_idx: {s_idx} | tens_place: {tens_place}"
                            
            if total == 0 or prev_val <= NUMERAL_TO_INT_MAP[curr_char] or NUMERAL_TO_INT_MAP[curr_char] - prev_val > 10:
                total += NUMERAL_TO_INT_MAP[curr_char]
            else: 
                total -= NUMERAL_TO_INT_MAP[curr_char]

            prev_val = NUMERAL_TO_INT_MAP[curr_char]
            s_idx += 1

        if total < 1 or total > 3999:
            raise ":("

        return total
    
sol = Solution()
if sol.romanToInt("III") != 3:
    raise # True
if sol.romanToInt("LVIII") != 58:               
    raise # True
if sol.romanToInt("MCMXCIV") != 1994:
    raise # True


          