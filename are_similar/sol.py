import copy
from typing import List 

class Solution:
    def shift_horizontal(self, arr, shift_left):
        if shift_left:
            arr = arr[1:] + arr[0:1]
        else: 
            arr = arr[-1:] + arr[0:-1]

        return arr

    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        dup_mat = copy.deepcopy(mat)

        for i in range(k):
            for j in range(len(dup_mat)):
                dup_mat[j] = self.shift_horizontal(dup_mat[j], j % 2 == 0)

       
        for i in range(len(mat)):
            if mat[i] != dup_mat[i]:
                return False

        return True 
    
sol = Solution()
print(sol.areSimilar([[2, 2], [25, 23]], 35)) # True