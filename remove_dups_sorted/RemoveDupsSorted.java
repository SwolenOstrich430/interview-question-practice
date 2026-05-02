/*
loop through list 
keep count of the 
*/
class RemoveDupsSolution {
    public int removeDuplicates(int[] nums) {
        int k = 2;
        for(int i = 2;i<nums.length;i++){
            if(nums[i]!=nums[k-2]){
                nums[k] = nums[i];
                k++;
            }
        }
        return k;
    }
}

class RemoveDupsSorted {
    public static void main(String[] args) {
        RemoveDupsSolution sol = new RemoveDupsSolution();
        int[] nums = new int[]{1,1,1,2,2,3};
        // int[] nums = new int[]{0,0,1,1,1,1,2,3,3};
        System.out.println(sol.removeDuplicates(nums));
    }
}

