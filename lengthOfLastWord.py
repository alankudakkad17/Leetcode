class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x=s.split(" ")
        x.reverse()
        for y in x:
            if y != "":
                leng=len(y)
                break
            else:
                continue
        return leng
