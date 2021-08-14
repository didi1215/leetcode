# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。 
# 
#  进阶：你能尝试使用一趟扫描实现吗？ 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：head = [1,2,3,4,5], n = 2
# 输出：[1,2,3,5]
#  
# 
#  示例 2： 
# 
#  
# 输入：head = [1], n = 1
# 输出：[]
#  
# 
#  示例 3： 
# 
#  
# 输入：head = [1,2], n = 1
# 输出：[1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中结点的数目为 sz 
#  1 <= sz <= 30 
#  0 <= Node.val <= 100 
#  1 <= n <= sz 
#  
#  Related Topics 链表 双指针 
#  👍 1504 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 快慢指针
        pre, cur = head, head
        for i in range(n):
            pre = pre.next
        # 这里需要注意，N的取值小于等于链表的长度。
        # 这里就需要排除下当右指针跑了N+1后，已经超出链表，那么代表链表长度与N相等。
        if not pre:
            return head.next
        while pre.next:
            pre = pre.next
            cur = cur.next
        cur.next = cur.next.next
        return head
# leetcode submit region end(Prohibit modification and deletion)
