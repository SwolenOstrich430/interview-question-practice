class SortedArraySearchSolution {
    public boolean search(int[] nums, int target) {
        if (nums == null || nums.length == 0) {
            return false;
        } else if (nums.length == 1) {
            return nums[0] == target;
        }

        int start = 0;
        int end = nums.length - 1;
        int numIters = 0;

        while (start <= end && numIters < nums.length) {
            if (nums[start] < target) {
                start++;
            } else if (nums[start] == target) {
                return true;
            }

            if (nums[end] > target) {
                end--;
            } else if (nums[end] == target) {
                return true;
            }

            numIters++;
        }

        return false;
    }
}

public class SortedArraySearch {
    public static void main(String[] args) {
        SortedArraySearchSolution sol = new SortedArraySearchSolution();
        int[] nums = new int[]{2,5,6,0,0,1,2};
        int target = 0;
        // int target = 3;
        System.out.println(sol.search(nums, target));
    }
}