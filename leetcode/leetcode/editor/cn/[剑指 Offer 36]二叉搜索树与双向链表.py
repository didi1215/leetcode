# 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。要求不能创建任何新的节点，只能调整树中节点指针的指向。 
# 
#  
# 
#  为了让您更好地理解问题，以下面的二叉搜索树为例： 
# 
#  
# 
#  
# 
#  
# 
#  我们希望将这个二叉搜索树转化为双向循环链表。链表中的每个节点都有一个前驱和后继指针。对于双向循环链表，第一个节点的前驱是最后一个节点，最后一个节点的后继是
# 第一个节点。 
# 
#  下图展示了上面的二叉搜索树转化成的链表。“head” 表示指向链表中有最小元素的节点。 
# 
#  
# 
#  
# 
#  
# 
#  特别地，我们希望可以就地完成转换操作。当转化完成以后，树中节点的左指针需要指向前驱，树中节点的右指针需要指向后继。还需要返回链表中的第一个节点的指针。 
# 
#  
# 
#  注意：本题与主站 426 题相同：https://leetcode-cn.com/problems/convert-binary-search-tree-
# to-sorted-doubly-linked-list/ 
# 
#  注意：此题对比原题有改动。 
#  Related Topics 栈 树 深度优先搜索 二叉搜索树 链表 二叉树 双向链表 
#  👍 282 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        # 性质：二叉搜索树的中序遍历为递增序列
        def dfs(cur):
            # 终止条件：当节点cur为空，代表越过叶节点，直接返回
            if not cur:
                return

            # 递归左子树
            dfs(cur.left)

            # 构建链表
            # #当pre为空，代表正在访问头节点，记录head
            if not self.pre:
                self.head = cur
            # #当pre不为空，修改双向节点引用
            else:
                self.pre.right = cur
                cur.left = self.pre
            # #保存cur，更新pre=cur
            self.pre = cur

            # 递归右子树
            dfs(cur.right)

        # 若root为空，直接返回
        if not root:
            return
        # 初始化空节点pre
        self.pre = None
        # 转化为双向链表
        dfs(root)
        # 构建循环链表:中序遍历结束后，head指向头节点，pre指向尾节点
        self.head.left = self.pre
        self.pre.right = self.head
        # 返回值:返回链表头节点head即可
        return self.head

        # leetcode submit region end(Prohibit modification and deletion)
