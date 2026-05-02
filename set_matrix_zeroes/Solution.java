import java.util.HashSet;
import java.util.Objects;
import java.util.Set;


class Point {
    private char axis;
    private int idx;

    public Point(char axis, int idx) {
        this.idx = idx;
        this.axis = axis;
    }

    public char getAxis() {
        return this.axis;
    }

    public int getIdx() {
        return this.idx;
    }

    @Override 
    public boolean equals(Object obj) {
        if (obj == null || this.getClass() != obj.getClass()) return false;

        Point other = (Point) obj;

        return (
            other.getAxis() == this.getAxis() && 
            other.getIdx() == this.getIdx()
        );
    }

    @Override 
    public int hashCode() {
        return Objects.hash(this.getAxis(), this.getIdx());
    }
}

class Solution1 {
    public void setZeroes(int[][] matrix) {
        Set<Point> futZeroes = new HashSet<>();

        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                if (matrix[i][j] == 0) {
                    futZeroes.add(new Point('y', i));
                    futZeroes.add(new Point('x', j));
                }
            }
        }

        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                if (i == 0 && j == 2) {
                    int b = 0;
                }
                if (futZeroes.contains(new Point('y', i)) || futZeroes.contains(new Point('x', j))) {
                    matrix[i][j] = 0;
                } 
            }
        }

        return;
    }
}


public class Solution {
    public static void main(String[] args) {
        int[][] ints = {{1,2,3,4},{5,0,7,8},{0,10,11,12},{13,14,15,0}};
        Solution1 sol = new Solution1();
        sol.setZeroes(ints);
    }
}