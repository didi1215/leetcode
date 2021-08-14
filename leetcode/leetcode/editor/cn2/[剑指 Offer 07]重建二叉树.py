# 输入某二叉树的前序遍历和中序遍历的结果，请构建该二叉树并返回其根节点。 
# 
#  假设输入的前序遍历和中序遍历的结果中都不含重复的数字。 
# 
#  
# 
#  示例 1: 
# 
#  
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
#  
# 
#  示例 2: 
# 
#  
# Input: preorder = [-1], inorder = [-1]
# Output: [-1]
#  
# 
#  
# 
#  限制： 
# 
#  0 <= 节点个数 <= 5000 
# 
#  
# 
#  注意：本题与主站 105 题重复：https://leetcode-cn.com/problems/construct-binary-tree-from-
# preorder-and-inorder-traversal/ 
#  Related Topics 树 数组 哈希表 分治 二叉树 
#  👍 517 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# solution
# https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof/solution/mian-shi-ti-07-zhong-jian-er-cha-shu-di-gui-fa-qin/
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def recur(root, left, right):
            if left > right:
                return
            node = TreeNode(preorder[root])
            i = dic[preorder[root]]
            node.left = recur(root + 1, left, i - 1)
            node.right = recur(i - left + root + 1, i + 1, right)
            return node

        dic = {}
        for i in range(len(inorder)):
            dic[inorder[i]] = i
        return recur(0, 0, len(inorder) - 1)
# leetcode submit region end(Prohibit modification and deletion)
