class Solution:
    def reverse(self, x: int) -> int:
        working_num = abs(int(x))
        reversed_num = 0 

        while working_num > 0:
            reversed_num = (reversed_num * 10) + (int(working_num) % int(10))
            working_num = int(working_num / 10)

            if (x < 0 and reversed_num > 2**31):
                return 0
            elif (x > 0 and reversed_num > 2**31):
                return 0

        if x < 0:
            reversed_num = reversed_num * -1

        return reversed_num
    
sol = Solution()
sol.reverse(-123)