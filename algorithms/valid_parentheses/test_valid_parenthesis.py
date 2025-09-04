import unittest
from valid_parentheses import Solution

class TestIsValid(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_valid_parentheses(self):
        self.assertTrue(self.sol.isValid("()"))
        self.assertTrue(self.sol.isValid("()[]{}"))
        self.assertTrue(self.sol.isValid("{[()]}"))

    def test_invalid_parentheses(self):
        self.assertFalse(self.sol.isValid("(]"))
        self.assertFalse(self.sol.isValid("([)]"))
        self.assertFalse(self.sol.isValid("("))
        self.assertFalse(self.sol.isValid("]"))

    def test_empty_string(self):
        self.assertIsNone(self.sol.isValid(""))

    def test_too_long_string(self):
        s = "()" * (10**4 + 1)
        self.assertIsNone(self.sol.isValid(s))

if __name__ == "__main__":
    unittest.main()