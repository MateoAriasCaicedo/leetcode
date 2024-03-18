class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        occurrences = {}

        for ch in s:
            if ch not in occurrences:
                occurrences[ch] = 1
            else:
                occurrences[ch] += 1

        for ch in t:
            if ch not in occurrences:
                return False
            else:
                occurrences[ch] -= 1

        for value in occurrences.values():
            if value != 0:
                return False

        return True
