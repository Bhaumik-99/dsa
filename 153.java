class Solution {
    public int findMin(int[] nums) {
        int left = 0, right = nums.length - 1;

        while (left < right) {
            int mid = left + (right - left) / 2;

            // If mid element is greater than right, minimum must be on right side
            if (nums[mid] > nums[right]) {
                left = mid + 1;
            } else {
                // Minimum could be at mid or to the left
                right = mid;
            }
        }

        // When loop ends, left == right and pointing to the smallest element
        return nums[left];
    }
}
