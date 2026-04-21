from typing import List 

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # [[1,3],[2,6],[8,10],[15,18]]
        # sort the array 
        # for each array 
        #   check if arr[i][0] in arr[i + 1] or arr[i][1] in arr[i + 1]
        #   if yes, get the min starting val and the max ending val and add to new array 
        #   only advance the new array index if there's no overlap

        sort_intervals = sorted(intervals)
        new_ranges = [sort_intervals[0]]

        for i in range(1, len(sort_intervals)):
            if ((sort_intervals[i][1] >= new_ranges[-1][0] and sort_intervals[i][1] <= new_ranges[-1][0]) or 
                (new_ranges[-1][1] >= sort_intervals[i][0] and new_ranges[-1][0] <= sort_intervals[i][0])):
                new_ranges[-1][0] = min(new_ranges[-1][0], sort_intervals[i][0])
                new_ranges[-1][1] = max(new_ranges[-1][1], sort_intervals[i][1])
            else:
                if sort_intervals[i] not in new_ranges:
                    new_ranges.append(sort_intervals[i])

        return new_ranges


sol = Solution()

test_cases = [
    [[[1,4], [2,3]], [[1, 4]]],
    [[[1,4], [0,4]], [[0, 4]]],
    [[[4,7],[1,4]], [[1,7]]]
]

for test_case in test_cases: 
    print(test_case[0])
    print(test_case[1])
    if sol.merge(test_case[0]) != test_case[1]:
        raise

