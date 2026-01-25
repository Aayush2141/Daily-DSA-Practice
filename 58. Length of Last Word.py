class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words=s.split()
        lens=len(words[-1])
        return lens
        