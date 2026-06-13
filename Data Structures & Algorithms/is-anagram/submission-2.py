class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sArray = list(s)
        tArray = list(t)

        for i in range(len(sArray)-1, -1, -1):
            selected = sArray[i]
            for j in tArray:
                if selected == j:
                    tArray.remove(j)
                    break

        if len(tArray) == 0:
            return True
        else:
            return False