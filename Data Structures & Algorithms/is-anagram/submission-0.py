class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        print(sorted(s),sorted(t))
        if sorted(s)==sorted(t):
            return True

        return False