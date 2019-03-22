"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

Accepted 530,857
Submissions 1,148,843
"""


class ListNode:
    """Definition for singly-linked list."""
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    1 判断列表是否存在 存在继续执行   不存在 return l1 or l2
    2 建立额外列表并产生两个结点 link 和 head ，link负责连接，head是最终返回结果 将 l1 和 l2 中的较小结点赋值到新建立列表
    3 开始循环比较l1和l2中的每一个元素 直到其中一个为空
    4 循环体外，为防止l1或者l2还有存在的元素，进行 link.next = l1 or l2 操作
    5 返回head头结点
    """
    def mergeTwoLists(self, l1, l2):
        if l1 and l2:
            if l1.val < l2.val:
                link = head = ListNode(l1.val)
                l1 = l1.next
            else:
                link = head = ListNode(l2.val)
                l2 = l2.next
            while l1 and l2:
                if l1.val < l2.val:
                    tmp = ListNode(l1.val)
                    tmp.next = link.next
                    link.next = tmp
                    link = tmp
                    l1 = l1.next
                else:
                    tmp = ListNode(l2.val)
                    tmp.next = link.next
                    link.next = tmp
                    link = tmp
                    l2 = l2.next
            link.next = l1 or l2
            return head
        else:
            return l1 or l2



first = ListNode(1)

print(first.val)

