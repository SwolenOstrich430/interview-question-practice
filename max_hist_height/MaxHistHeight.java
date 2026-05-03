class MaxHistHeightSolution {
    public int largestRectangleArea(int[] heights) {
        int currMax = 0;
        int currHeight = heights[0];

        for (int i = 0; i < heights.length; i++) {
            currHeight = heights[i];

            for (int j = i; j < heights.length; j++) {
                if (heights[j] == 0) {
                    break;
                }

                if (heights[j] < currHeight) {
                    currHeight = heights[j];
                }

                if (((j - i + 1) * currHeight) > currMax) {
                    currMax = (j - i + 1) * currHeight;
                }
            }
        }

        return currMax;
    }
}

public class MaxHistHeight {
    public static void main(String[] args) {
        MaxHistHeightSolution sol = new MaxHistHeightSolution();
        int[] heights = {2,1,5,6,2,3};
        System.out.println(sol.largestRectangleArea(heights));
    }
}