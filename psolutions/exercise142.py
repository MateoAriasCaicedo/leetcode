class Solution(object):

    def isAnagram(self, s: str, t: str) -> bool:
        occurences = {}

        for ch in s:
            if not ch in occurences:
                occurences[ch] = 1
            else:
                occurences[ch] += 1

        for ch in t:
            if not ch in occurences:
                return False
            else:
                occurences[ch] -= 1

        for value in occurences.values():
            if value != 0:
                return False

        return True

print(Solution().isAnagram("abc", "acb"))