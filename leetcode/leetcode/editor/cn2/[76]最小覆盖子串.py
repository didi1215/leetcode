# 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。 
# 
#  
# 
#  注意： 
# 
#  
#  对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。 
#  如果 s 中存在这样的子串，我们保证它是唯一的答案。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "a", t = "a"
# 输出："a"
#  
# 
#  示例 3: 
# 
#  
# 输入: s = "a", t = "aa"
# 输出: ""
# 解释: t 中两个字符 'a' 均应包含在 s 的子串中，
# 因此没有符合条件的子字符串，返回空字符串。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length, t.length <= 105 
#  s 和 t 由英文字母组成 
#  
# 
#  
# 进阶：你能设计一个在 o(n) 时间内解决此问题的算法吗？ Related Topics 哈希表 字符串 滑动窗口 
#  👍 1257 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.defaultdict(int)  # 记录t中字符的出现次数
        window = collections.defaultdict(int)  # 记录窗口中字符的出现次数
        for c in t:
            need[c] += 1
        left, right = 0, 0  # 初始化窗口为0
        valid = 0  # 用于记录window中出现了几个t中字符
        # 如t='abc',window = 'abb',valid = 2
        # 记录最小覆盖子串的起始索引和长度
        start = 0
        length = len(s) + 1

        while right < len(s):
            c = s[right]  # 即将加入window的字符c
            right += 1  # 右移窗口
            if c in need:
                window[c] += 1
                # window中字符c的出现次数已达到need时，valid进行更新
                if window[c] == need[c]:
                    valid += 1

                # 判断左侧边界是否需要收缩
                while valid == len(need):
                    if right - left < length:
                        start = left
                        length = right - left

                    # d是将移出窗口的字符
                    d = s[left]
                    # 左移窗口
                    left += 1
                    if d in need:
                        # 若删除的字符数量满足need数量，valid减少1
                        if window[d] == need[d]:
                            valid -= 1
                        window[d] -= 1
        if length == len(s) + 1:
            return ''
        else:
            return s[start:start + length]

# leetcode submit region end(Prohibit modification and deletion)
