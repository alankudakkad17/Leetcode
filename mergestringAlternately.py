class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word=""
        min_len = min(len(word1), len(word2))
        for i in range(min_len):
            word+=word1[i]+word2[i]
        word+=word1[min_len:]+word2[min_len:]
        return word

#besser solution
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []

        for a, b in zip(word1, word2):
            merged.append(a + b)
        
        merged.append(word1[len(word2):])
        merged.append(word2[len(word1):])

        return "".join(merged)
