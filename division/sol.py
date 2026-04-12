class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # can't use divide, multiplication, or mods 
        # but can use subtraction? 
        # handle if never gets in while loop
        div = 0 
        dup_dividend = abs(int(dividend))

        while dup_dividend >= abs(divisor):
            div += 1
            dup_dividend -= abs(divisor) 

        if (divisor < 0 and dividend >= 0) or (divisor >= 0 and dividend < 0):
            div = div * -1

        return div 
    
sol = Solution()

test_cases = [
    ((-1, 1), -1),
    ((10, 3), 3),
    ((7, -3), -2),
    ((0, 1), 0),
    ((1, 1), 1),
    ((-1, -1), 1),
    ((-2147483648, -1), 2147483647)
]

for test_case in test_cases:
    print(f"test_case[0]: {test_case[0]}")
    print(f"test_case[1]: {test_case[1]}")
    print(f"sol.divide(test_case[0][0], test_case[0][1]): {sol.divide(test_case[0][0], test_case[0][1])}")

    if sol.divide(test_case[0][0], test_case[0][1]) != test_case[1]:
        raise # True