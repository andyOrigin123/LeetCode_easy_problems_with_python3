"""
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Given nums = [1,1,2], Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.

Example 2:
Given nums = [0,0,1,1,1,2,2,3,3,4], Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.

Clarification:
Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++)
{
    print(nums[i]);
}
Accepted 544,365
Submissions 1,363,592
"""


class Solution:
    """
    1 判断nums是否为空，空 return 0 否则 继续执行接下来逻辑
    2 len(nums) > 0 进入循环体 为防止越界问题，循化终止条件 设置为 len_of_nums -1
    3 逐一比较nums中元素是否相等，相等 index += 1 后 跳过接下来的循环体
    4 不相等，nums[cnts] = nums[i+1]后，cnts += 1
    5 循环结束，返回cnts
    """
    def removeDuplicates(self, nums):
        i = 0
        cnts = 1
        len_of_nums = len(nums)
        if len_of_nums > 0:
            while i < len_of_nums-1:
                if nums[i] == nums[i+1]:
                    i += 1
                    continue
                else:
                    nums[cnts] = nums[i+1]
                    cnts += 1
                i += 1
            return cnts
        else:
            return 0


list1 = [1, 1, 2]
list2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
solution = Solution()
len_unique = solution.removeDuplicates(list2)
for i in range(len_unique):
    print(list2[i])



