# 给你一个字符串 s，找到 s 中最长的回文子串。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "cbbd"
# 输出："bb"
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "a"
# 输出："a"
#  
# 
#  示例 4： 
# 
#  
# 输入：s = "ac"
# 输出："a"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 1000 
#  s 仅由数字和英文字母（大写和/或小写）组成 
#  
#  Related Topics 字符串 动态规划 
#  👍 3936 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if size == 1:
            return s
        dp = [[False for _ in range(size)] for _ in range(size)]
        max_len = 1
        start = 0
        # dp[i][j]表示s[i:j+1]是否为回文子串
        for j in range(1, size):
            for i in range(j):
                # 当i==j时一定回文
                # j-i==1 j-i==2时，s[i]==s[j]则是回文
                if j - i <= 2:
                    if s[i] == s[j]:
                        dp[i][j] = True
                        cur_len = j - i + 1
                else:
                    # 头尾相等且掐头去尾还是回文
                    if s[i] == s[j] and dp[i + 1][j - 1]:
                        dp[i][j] = True
                        cur_len = j - i + 1
                if dp[i][j]:
                    if cur_len > max_len:
                        max_len = cur_len
                        start = i
        return s[start:start + max_len]
# leetcode submit region end(Prohibit modification and deletion)
