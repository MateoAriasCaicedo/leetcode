package main;

import java.util.HashMap;

class Solution {

  public int[] twoSum(int[] nums, int target) {
    var previousNumbers = new HashMap<Integer, Integer>();
    int[] output = new int[2];

    for (int i = 0; i < nums.length; i++) {
      int difference = target - nums[i];
      Integer differenceIndex = previousNumbers.get(difference);

      if (differenceIndex != null) {
        output[0] = i;
        output[1] = differenceIndex;
      }

      previousNumbers.put(nums[i], i);
    }

    return output;
  }

  public static void main(String[] args){
    new Solution().twoSum(new int[]{2,7,11,15}, 9);
  }
}
