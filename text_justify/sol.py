import Math
from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        curr_word = []
        curr_length = 0
        final_words = []
        idx = 0 

        while idx < len(words):
            if curr_length + len(curr_word) + len(words[idx]) > maxWidth:
                final_words.append(
                    self.justify_words(curr_word, curr_length, maxWidth)
                )
                curr_word = []    
                curr_length = 0
            
            curr_word.append(words[idx])
            curr_length += len(words[idx])
            idx += 1

        if len(curr_word) > 0:
            final_words.append(
                self.justify_words(curr_word, curr_length, maxWidth, "left")
            )

        return final_words 

    def justify_words(self, words, length, width, alignment="middle"):
        remaining_length = width - length 
        spaces_needed = round(remaining_length / max(1, (len(words) - 1)))
        remainder = remaining_length % spaces_needed
        new_word = ""

        for i in range(len(words)):
            if i == len(words) - 1 and alignment != "left":
                new_word += words[i]
            elif i < len(words) - 2:
                new_word += f"{words[i]}{" " * spaces_needed}"
            else:   
                spaces_needed = remainder if remainder > 0 else spaces_needed
                new_word += f"{words[i]}{" " * spaces_needed}"


        return new_word


sol = Solution()

test_cases = [
    [["what  you can do","for your country"], 20, ["what  you can do","for your country"]],
    [["own","reason","for","existing."], 17, []],
    [["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20],
    [["This", "is", "an", "example", "of", "text", "justification."], 16,[] ]
]

for test_case in test_cases: 
    if sol.fullJustify(test_case[0], test_case[1]) != test_case[2]:
        raise 