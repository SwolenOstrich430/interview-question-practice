from typing import List 

class Solution:
    def countAndSay(self, n: int) -> str:
        if n <= 0: 
            return ""

        curr_count = 0
        curr_word = "1"
        new_word = ""
        curr_num = None

        for i in range(1, n):
            for j in range(len(curr_word)):
                if curr_num is None or curr_num == curr_word[j]:
                    curr_count += 1
                    curr_num = curr_word[j]
                
                if j == len(curr_word) - 1 or curr_num != curr_word[j + 1]: 
                    new_word += f"{curr_count}{curr_num}"
                    curr_num = None
                    curr_count = 0



            curr_word = new_word 
            new_word = "" 
            curr_count = 0
            curr_num = None

        return curr_word
            



sol = Solution()

test_cases = [
    [0, ""],
    [1, "1"],
    [2, "11"],
    [3, "21"],
    [4, "1211"],
    [5, "111221"]
]

for test_case in test_cases:
    print(test_case[0])
    print(test_case[1])

    if sol.countAndSay(test_case[0]) != test_case[1]:
        raise