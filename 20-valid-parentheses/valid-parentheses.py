class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = []

        

        for ch in s:

            # Opening bracket
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)

            # Closing bracket
            else:
                if not stack:
                    return False

                top = stack.pop()

                if ch == ')' and top != '(':
                    return False

                if ch == '}' and top != '{':
                    return False

                if ch == ']' and top != '[':
                    return False

        # Stack empty hona chahiye
        return len(stack) == 0
        