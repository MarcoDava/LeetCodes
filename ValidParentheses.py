class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for string in s:
            print(string)
            if string == "(" or string=="[" or string=="{":
                stack.append(string)
            if string == ")":
                if stack:
                    if stack.pop() != "(":
                        return False
                else:
                    return False
            if string == "}":
                if stack:
                    if stack.pop() != "{":
                        return False
                else:
                    return False
            if string == "]":
                if stack:
                    if stack.pop() != "[":
                        return False
                else:
                    return False
        if stack:
            return False
        return True
