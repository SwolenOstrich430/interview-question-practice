import java.util.ArrayList;
import java.util.List;


class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> subsets = new ArrayList<>();
        setSubsets(subsets, nums, new ArrayList<>(), 0);
        return subsets;
    }

    public void setSubsets(
        List<List<Integer>> subsets,  
        int[] nums,
        List<Integer> currSub,
        int startIdx
    ) {
        subsets.add(new ArrayList<>(currSub));

        if (currSub.size() == nums.length) {
            return;
        }

        for (int i = startIdx; i < nums.length; i++) {
            currSub.add(nums[i]);
            setSubsets(subsets, nums, currSub, i + 1);
            currSub.remove(currSub.size() - 1);
        }
    }
}