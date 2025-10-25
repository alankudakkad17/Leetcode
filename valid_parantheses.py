class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for x in s:
            if(x=="(" or x=="{" or x=="["):
                stack.append(x)
            elif(x==")"):
                if(stack!=[] and stack[-1]=="("):
                    y=stack.pop(-1)
                else:
                    return False
                    break
            elif(x=="}"):
                if(stack!=[] and stack[-1]=="{"):
                    y=stack.pop(-1)
                else:
                    return False
                    break
            elif(x=="]"):
                if(stack!=[] and stack[-1]=="["):
                    y=stack.pop(-1)
                else:
                    return False
                    break
            
        if(stack==[]):
            return True
        else:
            return False

        
