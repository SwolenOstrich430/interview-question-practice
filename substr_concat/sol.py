from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        self.combos = []

        if (all(word in s for word in set(words))):
            for i in range(len(words)):
                self.find_substrings_helper(
                    s, 
                    words[0:i] + words[i+1:], 
                    i, 
                    words[i]
                )

        return self.combos 

    def find_substrings_helper(self, s, words, i, curr_word): 
        if i >= len(words): 
            i = 0 
        
        if len(words) == 0:
            if curr_word in s and s.index(curr_word) not in self.combos:
                curr_index = s.index(curr_word)
                self.combos.append(curr_index)

                while curr_word in s[curr_index + 1:]:
                    if curr_index in self.combos:
                        curr_index = s.index(curr_word, curr_index + 1)
                        self.combos.append(curr_index)

            return 

        for k in range(len(words)): 
            self.find_substrings_helper(
                s, 
                words[0:k] + words[k+1:], 
                i + 1, 
                curr_word + words[k]
            )


test_cases = [
    ("wordgoodgoodgoodbestword", ["word","good","best","word"], []),
    ("foobarfoobar", ["foo","bar"], [0,6]),
    ("barfoofoobarthefoobarman", ["bar","foo","the"], [6,9,12]),
    ("barfoothefoobarman", ["foo","bar"], [0,9]),
    ("wordgoodgoodgoodbestword", ["word","good","best","word"], []),
    ("barfoofoobarthefoobarman", ["bar","foo","the"], [6,9,12]),
]

sol = Solution()

for test_case in test_cases:
    print(f"test_case[0]: {test_case[0]}")
    print(f"test_case[1]: {test_case[1]}")
    print(f"test_case[2]: {test_case[2]}")
    print(f"sol.findSubstring(test_case[0], test_case[1]): {sol.findSubstring(test_case[0], test_case[1])}")

    if sol.findSubstring(test_case[0], test_case[1]).sort() != test_case[2].sort():
        raise # True
