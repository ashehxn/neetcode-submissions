class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sArray = list(s)
        tArray = list(t)

        sArray.sort()
        tArray.sort()

        for i in range(0, len(sArray), 1):
            if sArray[i] != tArray[i]:
                return False
        return True