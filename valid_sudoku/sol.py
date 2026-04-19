from typing import List 

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        vert_mem = {}
        horiz_mem = {}
        grid_mem = {}
        block_coords = None 

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] != "." and board[i][j] in horiz_mem:
                    return False
                
                if board[j][i] != "." and board[j][i] in vert_mem:
                    return False 

                block_coords = (int(i / 3), int(j / 3))
                if block_coords not in grid_mem:
                    grid_mem[block_coords] = {}

                if board[i][j] != "." and board[i][j] in grid_mem[block_coords]:
                    return False 

                grid_mem[block_coords][board[i][j]] = True
                horiz_mem[board[i][j]] = True 
                vert_mem[board[j][i]] = True

            horiz_mem.clear()
            vert_mem.clear()

        return True 
    
    
sol = Solution()

test_cases = []
test_cases.append((
    [[".",".",".",".","5",".",".","1","."],
    [".","4",".","3",".",".",".",".","."],
    [".",".",".",".",".","3",".",".","1"],
    ["8",".",".",".",".",".",".","2","."],
    [".",".","2",".","7",".",".",".","."],
    [".","1","5",".",".",".",".",".","."],
    [".",".",".",".",".","2",".",".","."],
    [".","2",".","9",".",".",".",".","."],
    [".",".","4",".",".",".",".",".","."]], 
    False
))

for test_case in test_cases:
    print(test_case[0])
    print(test_case[1])

    if sol.isValidSudoku(test_case[0]) != test_cases[1]:
        raise 


        

