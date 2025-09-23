# VALID PARENTHESES 
# You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.
# The input string s is valid if and only if:
# 1. Every open bracket is closed by the same type of close bracket.
# 2. Open brackets are closed in the correct order.
# 3. Every close bracket has a corresponding open bracket of the same type.
# Return true if s is a valid string, and false otherwise.

class Solution:
    def isValid(self, s: str) -> bool:
        hashMap = {"}":"{", "]":"[", ")":"("} # Map the opening parentheses to the closing ones

        stack = [] # Initialize stack

        for i, bracket in enumerate(s): 
            if bracket in "{([": # Keep going if an opening bracket
                stack.append(bracket)
            else:
                if stack: # While there closing brackets in the stack
                    # If closing bracket does matches the opening at the top of stack
                    if hashMap[bracket] == stack[-1]: 
                        stack.pop() # Remove the opening bracket from the stack
                    else:
                        return False # Invalid matching
                else:
                    return False # String s began with closing bracket(s)
        return not stack # If stack is empty, return True - all brackets matched
            
# Time complexity: O(n)
# Space complexity: O(n)
