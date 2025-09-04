# Valid Parenthesis Solution
![Python tests](https://github.com/eddo426/python-portfolio/actions/workflows/python-tests.yml/badge.svg)
![Coverage](https://img.shields.io/codecov/c/github/eddo426/python-portfolio)
![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)

This project implements the classic **Valid Parenthesis** algorithmic problem in Python.

## Problem Statement
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

**Constraints:**
- `1 <= s.length <= 104`
- `s` consists of parentheses only `'()[]{}'`.

## Solution
The algorithm uses a stack to validate balanced parentheses:
1. Iterate through each character in the string.
2. If the character is an opening bracket ((, [, {), push it onto the stack.
3. If the character is a closing bracket (), ], }), check the top of the stack:
- If the stack is empty, or the top does not match the corresponding opening bracket, return False.
- Otherwise, pop the stack.
4. At the end, if the stack is empty, return True. Otherwise, return False.

Complexity Analysis:
- Time Complexity: O(n), where n is the length of the string (each character is pushed/popped at most once).
- Space Complexity: O(n), for storing unmatched opening brackets in the stack.

## Examples
```python
s = "{[]}"
Solution().isValid(s)
# Output: True

s = "([)]"
Solution().isValid(s)
# Output: False