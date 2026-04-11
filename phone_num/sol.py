from typing import List

NUM_LETTER_MAP = {
    2: 'abc',
    3: 'def',
    4: 'ghi',
    5: 'jkl',
    6: 'mno',
    7: 'pqrs',
    8: 'tuv',
    9: 'wxyz',
}

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.combos = []
        self._letter_combinations_helper(digits, 0, "")

        return self.combos

    def _letter_combinations_helper(self, digits, i, curr_combo) -> List[str]:
        if i >= len(digits):
            if curr_combo not in self.combos and len(curr_combo) == len(digits):
                self.combos.append(curr_combo)

            return 

        for letter in NUM_LETTER_MAP[int(digits[i])]:
            self._letter_combinations_helper(
                digits, 
                i + 1, 
                curr_combo + letter
            )


test_cases = [
    ("23", ["ad","ae","af","bd","be","bf","cd","ce","cf"]),
    ("", []),
    ("2", ["a","b","c"]),   
]
        
sol = Solution()

for test_case in test_cases:
    print(f"test_case[0]: {test_case[0]}")
    print(f"test_case[1]: {test_case[1]}")
    print(f"sol.letterCombinations(test_case[0]): {sol.letterCombinations(test_case[0])}")

    if sol.letterCombinations(test_case[0]).sort() != test_case[1].sort():
        raise # True

