class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram={}
        for s in strs:
            sorted_word="".join(sorted(s))
            if sorted_word in anagram:
                anagram[sorted_word].append(s)
            else:
                anagram[sorted_word]=[s]
        return list(anagram.values())
