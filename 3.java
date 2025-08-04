class Solution {
    public int lengthOfLongestSubstring(String s) {
        int[] index = new int[128];
        int left = 0, maxLen = 0;
        for (int right = 0; right < s.length(); right++) {
            left = Math.max(index[s.charAt(right)], left);
            maxLen = Math.max(maxLen, right - left + 1);
            index[s.charAt(right)] = right + 1;
        }
        return maxLen;
    }
}
