class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True 

        return self.canBeEqualHelper(s1, s2, 0)

    def canBeEqualHelper(self, s1, s2, index):
        if index + 2 > len(s1) - 1:
            return s1 == s2
            
        temp = s1[index + 2:index + 3]
        temp1 = s1[index:index+1]
        s1_new = s1[:index] + temp + s1[index + 1:index + 2] + temp1 + s1[index + 3:]

        if s1_new == s2 or s1 == s2:
            return True 

        return (
            self.canBeEqualHelper(s1, s2, index + 1) or 
            self.canBeEqualHelper(s1_new, s2, index + 1)
        )
    

sol = Solution()
print(sol.canBeEqual("ifjz", "jzfi")) # True
print(sol.canBeEqual("abc", "bca")) # False