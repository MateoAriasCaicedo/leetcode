import java.util.HashSet;

class Solution {
    public boolean containsDuplicate(int[] nums) {
        var previus = new HashSet<Integer>();

        for (Integer n : nums) {
            if (!previus.add(n)) { // Returns false when the set already contains the element.
                return true;
            }
        }

        return false;
    }
}