class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result=""
        v=sorted(strs,key=len)
        small=len(v[0])
        w=v[0]
        for i in range(0,small):
            for y in strs:
                if w[i]!=y[i]:
                    return result
            result=result+y[i]
        return result
        
