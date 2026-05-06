import java.util.Arrays;

class Solution {
    public int hIndex(int[] citations) {
        if (citations.length == 0) {
            return 0;
        } else if (citations.length == 1) {
            return Math.min(citations[0], 1);
        }

        Arrays.sort(citations);
        int currMax = 0;
        int citationsAboveZero = 0;

        for (int i = 0; i < citations.length; i++) {
            if (citations[i] == 0) {
                continue;
            } 
         
            currMax = Math.max(
                currMax, 
                Math.min(citations[i], citations.length - i)
            );
        }

        return currMax;
    }
}