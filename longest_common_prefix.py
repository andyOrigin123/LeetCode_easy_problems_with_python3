"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Note: All given inputs are in lowercase letters a-z.

Accepted 425,015
Submissions 1,283,258
"""


class Solution:
    """
    1 寻找最小长度的字符串
    2 按照该字符串长度安对应位置取出每个字符串中的字符
    3 利用set去重
    4 返回结果
    """
    def len_str(self, str):
        return len(str)

    def longestCommonPrefix(self, strs):
        unique = list(set(strs))
        if len(unique) >= 1:
            min_len = min(list(map(self.len_str, unique)))
            res = ''
            if min_len:
                for i in range(min_len):
                    tmp_list = []
                    for ele in unique:
                        if ele[i]:
                            tmp_list.append(ele[i])
                    if len(set(tmp_list)) != 1:
                        return res
                    else:
                        res += str(tmp_list[0])
                return res
            else:
                return ''
        return ''

