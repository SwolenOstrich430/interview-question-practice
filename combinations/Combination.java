import java.util.ArrayList;
import java.util.List;


class CombinationsSol {
    private List<List<Integer>> combos; 

    public CombinationsSol() {
        this.combos = new ArrayList<>();
    }

    public List<List<Integer>> combine(int n, int k) {
        setCombos(n, k, new ArrayList<Integer>());
        return combos;
    }

    public void setCombos(int n, int k, ArrayList<Integer> currCombo) {
        if (currCombo.size() == k) {
            this.combos.add(new ArrayList<>(currCombo));
            return;
        }

        for (int i = 1; i <= n; i++) {
            currCombo.add(i);
            setCombos(n, k, currCombo);
            currCombo.remove(currCombo.size() - 1);
        }
        
        return;
    }
}

class Combination {
    public static void main(String[] args) {
        CombinationsSol sol = new CombinationsSol();
        System.out.println(sol.combine(4, 2));
    }
}