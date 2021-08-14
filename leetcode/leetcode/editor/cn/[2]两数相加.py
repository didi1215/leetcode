# 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。 
# 
#  请你将两个数相加，并以相同形式返回一个表示和的链表。 
# 
#  你可以假设除了数字 0 之外，这两个数都不会以 0 开头。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：l1 = [2,4,3], l2 = [5,6,4]
# 输出：[7,0,8]
# 解释：342 + 465 = 807.
#  
# 
#  示例 2： 
# 
#  
# 输入：l1 = [0], l2 = [0]
# 输出：[0]
#  
# 
#  示例 3： 
# 
#  
# 输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# 输出：[8,9,9,9,0,0,0,1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  每个链表中的节点数在范围 [1, 100] 内 
#  0 <= Node.val <= 9 
#  题目数据保证列表表示的数字不含前导零 
#  
#  Related Topics 递归 链表 数学 
#  👍 6559 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 先将l1和l2头节点的值加起来赋值给新链表的头节点
        head = ListNode(l1.val + l2.val)
        cur = head
        # 遍历两个链表，只要有一个链表还没有遍历到末尾，就继续遍历
        while l1.next or l2.next:
            l1 = l1.next if l1.next else ListNode()
            l2 = l2.next if l2.next else ListNode()
            # 每次遍历生成一个当前节点cur的下一个节点，其值为两链表对应节点的和再加上当前节点cur产生的进位
            cur.next = ListNode(l1.val + l2.val + cur.val // 10)
            # 更新进位后的当前节点cur的值
            cur.val = cur.val % 10
            cur = cur.next
        # 循环结束后，因为首位可能产生进位，因此如果cur.val是两位数的话，新增一个节点
        if cur.val >= 10:
            cur.next = ListNode(cur.val // 10)
            cur.val = cur.val % 10
        # 返回头节点
        return head
# leetcode submit region end(Prohibit modification and deletion)
