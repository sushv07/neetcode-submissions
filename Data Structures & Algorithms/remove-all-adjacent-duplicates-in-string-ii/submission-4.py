class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []  # Stores [character, consecutive count]

        for c in s:
            # If the stack is not empty and the last character is the   same,
            # increase its consecutive count
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
            # Otherwise, start a new character group with count 1
            else:
                stack.append([c, 1])
            # If this recent group reaches k characters, remove the whole group
            if stack[-1][1] == k:
                stack.pop()

        result = []

        # Rebuild the remaining characters from the stack
        for ch, count in stack:
            result.append(ch * count)

        # Join all remaining groups into the final string
        return ''.join(result)