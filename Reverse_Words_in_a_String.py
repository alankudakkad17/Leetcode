class Solution:
    def reverseWords(self, s: str) -> str:
        x=s.split()
        a=""
        for y in x[::-1]:
            a+=y+" "
        a=a.strip()
        return a
