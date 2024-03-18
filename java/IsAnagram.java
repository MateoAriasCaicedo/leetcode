class Solution {

    public boolean isAnagram(String s, String t) {
        int n = s.length();
        if (n != t.length()) {
            return false;
        }

        int[] asciiHashS = new int[26];
        int[] asciiHashT = new int[26];

        for (int i = 0; i < n; i++) {
            int asciiS = s.charAt(i);
            int asciiT = t.charAt(i);

            asciiHashS[asciiS % 26] += 1;
            asciiHashT[asciiT % 26] += 1;
        }

        for (int i = 0; i < 26; i++) {
            if (asciiHashT[i] != asciiHashS[i]) {
                return false;
            }
        }

        return true;
    }
}
