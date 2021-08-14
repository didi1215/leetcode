# 给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。 
# 
#  单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。 
# 
#  
# 
#  例如，在下面的 3×4 的矩阵中包含单词 "ABCCED"（单词中的字母已标出）。 
# 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "AB
# CCED"
# 输出：true
#  
# 
#  示例 2： 
# 
#  
# 输入：board = [["a","b"],["c","d"]], word = "abcd"
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= board.length <= 200 
#  1 <= board[i].length <= 200 
#  board 和 word 仅由大小写英文字母组成 
#  
# 
#  
# 
#  注意：本题与主站 79 题相同：https://leetcode-cn.com/problems/word-search/ 
#  Related Topics 数组 回溯 矩阵 
#  👍 372 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, k):
            # 返回 falsefalse ： (1) 行或列索引越界 或
            # (2) 当前矩阵元素与目标字符不同 或
            # (3) 当前矩阵元素已访问过
            # 返回 truetrue ： k = len(word) - 1 ，即字符串 word 已全部匹配。
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            # 标记当前矩阵元素： 将 board[i][j] 修改为 空字符 '' ，代表此元素已访问过，防止之后搜索时重复访问。
            # 搜索下一单元格： 朝当前元素的 上、下、左、右 四个方向开启下层递归，使用 或 连接 （代表只需找到一条可行路径就直接返回，不再做后续 DFS ），并记录结果至 res 。
            # 还原当前矩阵元素： 将 board[i][j] 元素还原至初始值，即 word[k] 。
            board[i][j] = ''
            res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            board[i][j] = word[k]
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False
# leetcode submit region end(Prohibit modification and deletion)
