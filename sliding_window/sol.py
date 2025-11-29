'''
    * calculate area = min(start_bar, end_bar) * (end_bar_index - start_bar_index)
    * keep track of the max area 
    * and check combinations of points, i and j, where j > i, j < len(height) and height[i] < height[j]
        - last part is how we short circuit to avoid having to check every single combo
'''
class Solution(object):
    def maxArea(self, height):
        start_idx = 0
        end_idx = len(height) - 1
        curr_max = 0 
        curr_area = 0

        while (start_idx < end_idx):
            curr_area = (end_idx - start_idx) * min(height[start_idx], height[end_idx])

            if curr_area > curr_max:
                curr_max = curr_area

            if height[start_idx] < height[end_idx]:
                start_idx += 1
            else: 
                end_idx -= 1

        return curr_max
        