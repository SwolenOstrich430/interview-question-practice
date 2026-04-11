class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.combos = []
        self._generate_parens_helper(n, "(")
        return self.combos 

    def _generate_parens_helper(self, n, curr_combo, is_open=False): 
        if len(curr_combo) == (n * 2):
            if curr_combo not in self.combos: # and self.isValid(curr_combo):
                self.combos.append(curr_combo)

            return 

        if curr_combo.count("(") < n:
            self._generate_parens_helper(n, curr_combo + "(", True)

        if curr_combo.count(")") < n and curr_combo.count("(") > curr_combo.count(")"):
            self._generate_parens_helper(n, curr_combo + ")", curr_combo.count("(") > curr_combo.count(")"))


sol = Solution()

test_cases = [
    (3, ["((()))","(()())","(())()","()(())","()()()"]),
    (1, ["()"]),
    (2, ["(())","()()"]),
]

for test_case in test_cases:
    print(f"test_case[0]: {test_case[0]}")
    print(f"test_case[1]: {test_case[1]}")
    print(f"sol.generateParenthesis(test_case[0]): {sol.generateParenthesis(test_case[0])}")

    if sol.generateParenthesis(test_case[0]).sort() != test_case[1].sort():
        raise # True