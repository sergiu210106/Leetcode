'''
20. Valid Parantheses

Given a string s containing just the characters (, ), {, }, [, ],
determine if the input string is valid.

An input string is valid if:
    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.
    3. Every closed bracket has a corresponding open bracket of
    the same type.
'''

class Solution:
    def isValid(self, s: str) -> bool:
        parantheses_dict = {
                "(" : 1, ")" : -1,
                "[" : 2, "]" : -2,
                "{" : 3, "}" : -3
                }
        queue = []
        for character in s:
            if queue and parantheses_dict[character] + parantheses_dict[queue[-1]] == 0 and parantheses_dict[queue[-1]] > 0:
                queue.pop()
            else:
                queue.append(character)

        return queue == []


if __name__ == '__main__':
    solution = Solution()
    print(solution.isValid("()"))
    print(solution.isValid("()[]{}"))
    print(solution.isValid("(]"))
    print(solution.isValid("([])"))
    print(solution.isValid("([)]"))
