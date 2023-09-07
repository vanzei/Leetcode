class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        Map = {")":"(", "]":"[", "}":"{"}
        for char in s:
            if char not in Map:
                stack.append(char)
                continue
            if not stack or stack[-1] != Map[char]:
                return False
            stack.pop()

        return not stack
