import itertools

DIGIT_MAPPINGS = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        mappings = []
        
        return self.letter_combinations_helper(
            digits,
            mappings
        )

    def letter_combinations_helper(
        self, 
        digits: str,
        mappings: list[str]
    ) -> list[str]:
        if not digits: 
            return mappings

        new_mappings = []
        curr_digits = self.get_digit_letter_mapping(digits[0])

        if not mappings: 
            new_mappings = curr_digits
        else: 
            for item1, item2 in itertools.product(mappings, curr_digits):
                new_mappings.append(f"{item1}{item2}")

        if len(digits) == 1:
            return new_mappings
        
        return self.letter_combinations_helper(
            digits[1:],
            new_mappings
        )

    def get_digit_letter_mapping(self, digit: str) -> str:
        return list(DIGIT_MAPPINGS[digit])
    
sol = Solution()
sol.letterCombinations("23")