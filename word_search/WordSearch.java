import java.util.List;
import java.util.ArrayList;
import java.util.HashMap;


class Coordinate {
    int x;
    int y;

    public static Coordinate from(Coordinate c) {
        return new Coordinate(c.x, c.y);
    }

    public Coordinate(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public int hashCode() {
        return this.x * 31 + this.y;
    }

    public boolean equals(Object o) {
        if (o == this) {
            return true;
        }

        if (!(o instanceof Coordinate)) {
            return false;
        }

        Coordinate c = (Coordinate) o;
        return this.x == c.x && this.y == c.y;
    }
}

class WordSearchSolution {
    public List<Coordinate> getPotentialStarts(char[][] board, char firstChar) {
        List<Coordinate> potentialStarts = new ArrayList<>();

        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[i].length; j++) {
                if (board[i][j] == firstChar) {
                    potentialStarts.add(new Coordinate(i, j));
                }
            }
        }

        return potentialStarts;
    }

    public boolean exist(char[][] board, String word) {
        if (word == null || word.isEmpty()) {
            return true;
        }

        List<Coordinate> potentialStarts = getPotentialStarts(
            board, word.charAt(0)
        );

        if (word.length() == 1) {
            return !potentialStarts.isEmpty();
        }

        String newWord = word.substring(1, word.length());
        for (Coordinate potentialStart : potentialStarts) {
            HashMap<Coordinate, Boolean> mem = new HashMap<>();
            mem.put(potentialStart, true);

            if (dfs(potentialStart, board, newWord, mem)) {
                return true;
            }
        }

        return false;
    }

    public boolean dfs(Coordinate coord, char[][] board, String word, HashMap<Coordinate, Boolean> mem) {
        if (word.isEmpty()) {
            return true;
        }

        char currChar = word.charAt(0);
        int wordLen = word.length();
        Coordinate newCoord;

        // look up
        if (coord.x > 0 && board[coord.x - 1][coord.y] == currChar) {
            newCoord = new Coordinate(coord.x - 1, coord.y);
            if (!mem.containsKey(newCoord)) {
                mem.put(Coordinate.from(newCoord), true);

                if (dfs(
                    new Coordinate(coord.x - 1, coord.y), 
                    board, 
                    word.substring(1, wordLen),
                    mem
                )) {
                    return true;
                }

                mem.remove(newCoord);
            }
        } 
        
        // look left 
        if (coord.y > 0 && board[coord.x][coord.y - 1] == currChar) {
            newCoord = new Coordinate(coord.x, coord.y - 1);

            if (!mem.containsKey(newCoord)) {
                mem.put(Coordinate.from(newCoord), true);

                if (dfs(
                    new Coordinate(coord.x, coord.y - 1), 
                    board, 
                    word.substring(1, wordLen),
                    mem
                )) {
                    return true;
                }

                mem.remove(newCoord);
            }
        }
        
        // look down
        if (coord.x < board.length - 1 && board[coord.x + 1][coord.y] == currChar) {
            newCoord = new Coordinate(coord.x + 1, coord.y);

            if (!mem.containsKey(newCoord)) {
                mem.put(Coordinate.from(newCoord), true);
                
                if (dfs(
                    new Coordinate(coord.x + 1, coord.y), 
                    board, 
                    word.substring(1, wordLen),
                    mem
                )) {
                    return true;
                }

                mem.remove(newCoord);
            }
        } 
        
        // look right
        if (coord.y < board[0].length - 1 && board[coord.x][coord.y + 1] == currChar) {
            newCoord = new Coordinate(coord.x, coord.y + 1);

            if (!mem.containsKey(newCoord)) {
                mem.put(Coordinate.from(newCoord), true);

                if (dfs(
                    new Coordinate(coord.x, coord.y + 1), 
                    board, 
                    word.substring(1, wordLen),
                    mem
                )) {
                    return true;
                }

                mem.remove(newCoord);
            }
        } 

        return false;
    }
}

public class WordSearch {
    public static void main(String[] args) {
        WordSearchSolution sol = new WordSearchSolution();
        char[][] board = new char[][]{
            {'A', 'B', 'C', 'E'},
            {'S', 'F', 'E', 'S'},
            {'A', 'D', 'E', 'E'}
        };
        // char[][] board = new char[][]{{'a', 'a'}};
        System.out.println(sol.exist(board, "ABCESEEEFS"));
    }
}