class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        pairs={
            ")":"(",
            "]":"[",
            "}":"{"
        }
        for x in s:
            if x in "{([":
                stack.append(x)
            else:
                if not stack:
                    return False
                if stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            
         return len(stack) == 0
        
