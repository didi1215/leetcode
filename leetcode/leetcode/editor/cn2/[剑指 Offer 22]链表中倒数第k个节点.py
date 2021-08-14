# 输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。 
# 
#  例如，一个链表有 6 个节点，从头节点开始，它们的值依次是 1、2、3、4、5、6。这个链表的倒数第 3 个节点是值为 4 的节点。 
# 
#  
# 
#  示例： 
# 
#  
# 给定一个链表: 1->2->3->4->5, 和 k = 2.
# 
# 返回链表 4->5. 
#  Related Topics 链表 双指针 
#  👍 218 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        #         快慢指针
        former, latter = head, head
        for i in range(k):
            # former和latter相差k
            former = former.next
        while former:
            # former = null时跳出
            former, latter = former.next, latter.next
        return latter
# leetcode submit region end(Prohibit modification and deletion)
