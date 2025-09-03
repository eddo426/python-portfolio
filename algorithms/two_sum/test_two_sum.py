import unittest
from two_sum import Solution

class TestTwoSum(unittest.TestCase):
    def test_example_case(self):
        self.assertEqual(Solution().twoSum([2, 7, 11, 15], 9), [0, 1])

    def test_no_solution(self):
        self.assertIsNone(Solution().twoSum([1, 2, 3], 10))

    def test_negative_numbers(self):
        self.assertEqual(Solution().twoSum([-1, -2, -3, -4, -5], -8), [2, 4])
        
if __name__ == "__main__":
    unittest.main()