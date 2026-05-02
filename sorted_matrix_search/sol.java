class MinWindowString {
    public boolean searchMatrix(int[][] matrix, int target) {
        /*
            1. find the row where the numbers start getting greater or equal
            2. if equal, return true 
            3. if never greater, return false 
            4. if found greater, exit loop and save i-- as the start index 
            5. loop through the row and find it 
        */

        int start_idx = matrix.length - 1;

        for (int i = 0; i < matrix.length; i++) {
            if (matrix[i][0] > target) {
                start_idx = i == 0 ? i : i - 1;
                break;
            } else if (matrix[i][0] == target) {
                return true;
            } else if (matrix.length == 1) {
                start_idx = i; 
                break;  
            } 
        }

        for (int i = 0; i < matrix[start_idx].length; i++) {
            if (matrix[start_idx][i] == target) {
                return true;
            }
        }

        return false;
    }
}

class Main {
    public static void main(String[] args) {
        int[][] ints = {{1,3,5,7},{10,11,16,20},{23,30,34,60}};
        MinWindowString sol = new MinWindowString();
        System.out.println(sol.searchMatrix(ints, 3));
    }
}