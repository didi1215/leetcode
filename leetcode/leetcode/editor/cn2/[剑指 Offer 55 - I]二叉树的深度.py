# 输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。 
# 
#  例如： 
# 
#  给定二叉树 [3,9,20,null,null,15,7]， 
# 
#      3
#    / \
#   9  20
#     /  \
#    15   7 
# 
#  返回它的最大深度 3 。 
# 
#  
# 
#  提示： 
# 
#  
#  节点总数 <= 10000 
#  
# 
#  注意：本题与主站 104 题相同：https://leetcode-cn.com/problems/maximum-depth-of-binary-tre
# e/ 
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 
#  👍 130 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # 层序遍历BFS，广度优先搜索，队列
        if not root:
            return 0
        res, queue = 0, [root]
        while queue:
            tmp = []
            for node in queue:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            queue = tmp
            res += 1
        return res
# leetcode submit region end(Prohibit modification and deletion)
