# Two Sum Solution
![Python tests](https://github.com/eddo426/python-portfolio/actions/workflows/python-tests.yml/badge.svg)
![Coverage](https://img.shields.io/codecov/c/github/eddo426/python-portfolio)
![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)

This project implements the classic **Two Sum** algorithmic problem in Python.

## Problem Statement
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

**Constraints:**
- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- Only one valid answer exists.
- You may not use the same element twice.

## Solution
- Uses a **hashmap** to track seen numbers.
- Runs in **O(n) time**, **O(n) space**.

## Example
```python
nums = [2, 7, 11, 15]
target = 9
Solution().twoSum(nums, target)
# Output: [0, 1]