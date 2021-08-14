# 请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。 
# 
#  例如，二叉树 [1,2,2,3,4,4,3] 是对称的。 
# 
#  1 
#  / \ 
#  2 2 
#  / \ / \ 
# 3 4 4 3 
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的: 
# 
#  1 
#  / \ 
#  2 2 
#  \ \ 
#  3 3 
# 
#  
# 
#  示例 1： 
# 
#  输入：root = [1,2,2,3,4,4,3]
# 输出：true
#  
# 
#  示例 2： 
# 
#  输入：root = [1,2,2,null,3,null,3]
# 输出：false 
# 
#  
# 
#  限制： 
# 
#  0 <= 节点个数 <= 1000 
# 
#  注意：本题与主站 101 题相同：https://leetcode-cn.com/problems/symmetric-tree/ 
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 
#  👍 213 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def compare(self, x, y):
        if not x and not y:
            return True
        if not x or not y:
            return False
        if x.val != y.val:
            return False
        return self.compare(x.left, y.right) and self.compare(x.right, y.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        res = True
        if root:
            res = self.compare(root.left, root.right)
        return res
# leetcode submit region end(Prohibit modification and deletion)
