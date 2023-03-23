class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 
        mapping=  {")":"(","]":"[","}":"{" }
        for char in s:
            if(char=='(' or char=='{' or char=='['): #if open insetr to stack
                stack.append(char)
            else: #this is a close bracket
                if(len(stack)==0):
                    return False
                last_element=stack.pop()
                if(last_element!=mapping[char]):
                    return False
        if(not stack):
            return True
                    


