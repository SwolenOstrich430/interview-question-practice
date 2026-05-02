import java.util.HashMap;


class MinWindowStringSolution {
    public String minWindow(String s, String t) {
        if (t.length() == 1 && s.contains(t)) {
            return t;
        }
        
        HashMap<String, Integer> char_count = new HashMap<>();

        for (int i = 0; i < t.length(); i++) {
            char_count.put(
                String.valueOf(t.charAt(i)), 
                char_count.getOrDefault(String.valueOf(t.charAt(i)), 0) + 1
            );
        }

        HashMap<String, Integer> c_char_count = new HashMap<>(char_count);
        int start_idx = -1;
        int curr_idx = 0;
        int second_letter_idx = -1;
        int min_start_idx = -1;
        int min_end_idx = -1;
        String curr_char;

        while (curr_idx < s.length()) {
            curr_char = String.valueOf(s.charAt(curr_idx));

            if (char_count.containsKey(curr_char)) {
                if (c_char_count.containsKey(curr_char)) {
                    c_char_count.put(
                        curr_char,
                        c_char_count.get(curr_char) - 1
                    );
                } 

                if (c_char_count.get(curr_char) != null && c_char_count.get(curr_char) == 0) {
                    c_char_count.remove(curr_char);
                }
                
                if (start_idx == -1) {
                    start_idx = curr_idx;
                } else if (second_letter_idx == -1) {
                    second_letter_idx = curr_idx;
                }
            }

            if (c_char_count.values().stream().allMatch(v -> v <= 0)) {
                if (min_start_idx == -1 || curr_idx - start_idx < min_end_idx - min_start_idx) {
                    min_start_idx = start_idx;
                    min_end_idx = curr_idx;
                }

                curr_idx = second_letter_idx;
                start_idx = -1;
                second_letter_idx = -1;
                c_char_count = new HashMap<>(char_count);
            } else {
                curr_idx++;
            }
        }

        if (min_start_idx == -1) {
            return "";
        }

        return s.substring(min_start_idx, min_end_idx + 1);
    }
}

class MinWindowStringSolution2 {
    public String minWindow(String s, String t) {
        if (t.length() == 1 && s.contains(t)) {
            return t;
        }
        
        int[] char_count = new int[128];
        for (int i = 0; i < t.length(); i++) {
            char_count[t.charAt(i)]++;
        }

        int start_idx = 0;
        int curr_idx = 0;
        int min_start_idx = -1;
        int min_end_idx = -1;
        int matchesRemaining = t.length();
        char curr_char;
        char[] s_char_arr = s.toCharArray();

        while (curr_idx < s.length()) {
            curr_char = s.charAt(curr_idx);

            if (char_count[curr_char] > 0) {
                char_count[curr_char]--;
                matchesRemaining--;
            }

            while (matchesRemaining == 0) {
                if (min_start_idx == -1 || curr_idx - start_idx < min_end_idx - min_start_idx) {
                    min_start_idx = start_idx;
                    min_end_idx = curr_idx;
                }

                if (char_count[s_char_arr[start_idx]]++ == 0) {
                    matchesRemaining++;
                }

                start_idx++;
            }

            curr_idx++;
        }

        if (min_start_idx == -1) {
            return "";
        }

        return s.substring(min_start_idx, min_end_idx + 1);
    }
}

class MinWindowStringSolution1 {
    public String minWindow(String s, String t) {
        if (s == null || t == null || s.length() == 0 || t.length() == 0 ||
                s.length() < t.length()) {
            return new String();
        }
        int[] map = new int[128];
        int count = t.length();
        int start = 0, end = 0, minLen = Integer.MAX_VALUE, startIndex = 0;
        /// UPVOTE !
        for (char c : t.toCharArray()) {
            map[c]++;
        }

        char[] chS = s.toCharArray();

        while (end < chS.length) {
            if (map[chS[end++]]-- > 0) {
                count--;
            }
            while (count == 0) {
                if (end - start < minLen) {
                    startIndex = start;
                    minLen = end - start;
                }
                if (map[chS[start++]]++ == 0) {
                    count++;
                }
            }
        }

        return minLen == Integer.MAX_VALUE ? new String() :
                new String(chS, startIndex, minLen);
    }
}

class MinWindowString1 {
    public static void main(String[] args) {
        MinWindowStringSolution2 sol = new MinWindowStringSolution2();
        System.out.println(sol.minWindow("ADOBECODEBANC", "ABC"));
        // System.out.println(sol.minWindow("bba", "ab"));
    }
}