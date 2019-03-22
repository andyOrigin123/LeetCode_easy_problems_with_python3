"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:
Input: "()"
Output: true

Example 2:
Input: "()[]{}"
Output: true

Example 3:
Input: "(]"
Output: false

Example 4:
Input: "([)]"
Output: false

Example 5:
Input: "{[]}"
Output: true

Accepted 537,811
Submissions 1,491,303
"""


class Solution:
    def __init__(self):
        self.left_lists = ["(", "[", "{"]
        self.right_lists = [")", "]", "}"]
        self.pair_parenthese = {"(": ")", "[": "]", "{": "}"}

    def isValid(self, s):
        left_tmp = []
        s_len = len(s)
        # 偶数
        if s_len > 0 and s_len % 2 == 0:
            for ele in s:
                if ele in self.left_lists:
                    left_tmp.append(ele)
                elif ele in self.right_lists:
                    if len(left_tmp):
                        left = self.pair_parenthese.get(left_tmp.pop())
                        if ele != left:
                            return False
                        elif ele == left and len(left_tmp) == 0 and ele == s[-1]:
                            return True
        # 奇数
        elif s_len % 2 != 0:
            return False
        # 其他
        else:
            return True
        return False
