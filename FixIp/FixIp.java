import java.util.ArrayList;
import java.util.List;

class FixIpSolution {

    public List<String> restoreIpAddresses(String s) {
        List<String> finalStrings = new ArrayList<>();
        StringBuilder sb = new StringBuilder();

        helper(s, finalStrings, sb, 0, 0);

        return finalStrings;
    }

    public void helper(String s, List<String> finalStrings, StringBuilder sb, int currIdx, int periodCount) {
        if (currIdx >= s.length() && periodCount == 4) {
            finalStrings.add(sb.toString());
            return;
        } else if (periodCount > 3) {
            return;
        } else if (s.length() - currIdx > (12 - (periodCount * 3))) {
            return;
        }

        for (int i = currIdx + 2; i >= currIdx; i--) {
            if (i >= s.length()) {
                continue;
            }

            if (Integer.parseInt(s.substring(currIdx, i + 1)) > 255) {
                continue;
            }
            
            int lastLen = i + 1 - currIdx;

            if (periodCount == 3) {
                sb.append(s.substring(currIdx, i + 1));
            } else { 
                lastLen++;
                sb.append(s.substring(currIdx, i + 1) + ".");
            }
            
            helper(s, finalStrings, sb, i + 1, periodCount + 1);
            sb.delete(sb.length() - lastLen, sb.length());
        }
    }
}

class FixIp {
    public static void main(String[] args) {
        FixIpSolution sol = new FixIpSolution();
        String s = "0000";
        System.out.println(sol.restoreIpAddresses(s));
    }
}