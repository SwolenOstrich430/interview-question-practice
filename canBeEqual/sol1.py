class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        for i in range(len(s1)):
            if s1[i] == s2[i]:
                continue 

            if s1[i] not in s2[i + 1:]:
                return False 
            
            index = None
            original_index = i
            while index is None and original_index < len(s1) - 1:
                try:
                    index = s1[original_index + 1:].index(s2[i]) + original_index + 1
                except ValueError:
                    return False
            
                original_index += 1
                if (index - i) % 2 != 0:
                    index = None 

            if index is None:
                return False 
            
            temp = s1[index:index + 1]
            s1 = s1[:i] + temp + s1[i + 1:index] + s1[i] + s1[index + 1:]

        return True


sol = Solution()
print(sol.checkStrings("abcdba", "cabdab")) # True
print(sol.checkStrings("abe", "bea")) # False
print(sol.checkStrings("ifjz", "jzfi")) # True