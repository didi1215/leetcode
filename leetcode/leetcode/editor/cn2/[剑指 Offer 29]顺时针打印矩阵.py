# 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。 
# 
#  
# 
#  示例 1： 
# 
#  输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
#  
# 
#  示例 2： 
# 
#  输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
#  
# 
#  
# 
#  限制： 
# 
#  
#  0 <= matrix.length <= 100 
#  0 <= matrix[i].length <= 100 
#  
# 
#  注意：本题与主站 54 题相同：https://leetcode-cn.com/problems/spiral-matrix/ 
#  Related Topics 数组 矩阵 模拟 
#  👍 281 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        res = []
        left = 0
        right = len(matrix[0]) - 1
        top = 0
        bottom = len(matrix) - 1
        while True:
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1
            if top > bottom:
                break
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            if right < left:
                break
            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1
            if top > bottom:
                break
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
            if left > right:
                break
        return res

# leetcode submit region end(Prohibit modification and deletion)
