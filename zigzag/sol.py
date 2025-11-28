
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        arr = [[None for _ in range(len(s))] for _ in range(numRows)]
        curr_s_index = 0
        x, y = 0, 0
        x_dir, y_dir = None, None

        while curr_s_index < len(s):
            arr[y][x] = s[curr_s_index]

            if y == numRows - 1:
                y_dir = -1
                x_dir = 1
            elif y == 0:
                y_dir = 1
                x_dir = 0

            y += y_dir
            x += x_dir
            curr_s_index += 1

        ret_str = ""
        for chars in arr:
            ret_str += "".join(list(filter(None, chars)))

        return ret_str
    
sol = Solution()
sol.convert("PAYPALISHIRING", 3)