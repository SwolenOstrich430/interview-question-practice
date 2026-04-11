OPEN_CLOSE_MAP = {
    '(': ')',
    ')': '(',
    '{': '}',
    '}': '{',
    '[': ']',
    ']': '['
}

class Solution:
    def isValid(self, s: str) -> bool:
        fifo = []

        for char in s: 
            if char in ['(', '{', '[']:
                fifo.insert(0, char)
            elif char in [')', '}', ']']:
                if len(fifo) == 0 or fifo[0] != OPEN_CLOSE_MAP[char]:
                    return False
                else: 
                    fifo = fifo[1:]
        
        return len(fifo) == 0