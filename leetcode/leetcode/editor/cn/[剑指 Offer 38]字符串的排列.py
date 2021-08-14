# 输入一个字符串，打印出该字符串中字符的所有排列。 
# 
#  
# 
#  你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。 
# 
#  
# 
#  示例: 
# 
#  输入：s = "abc"
# 输出：["abc","acb","bac","bca","cab","cba"]
#  
# 
#  
# 
#  限制： 
# 
#  1 <= s 的长度 <= 8 
#  Related Topics 字符串 回溯 
#  👍 400 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def permutation(self, s: str) -> List[str]:
        # 递归
        c = list(s)
        res = []

        # 递归参数：当前固定位x
        def dfs(x):
            # 当x=len(c)-1时，代表所有位已固定，只剩最后一位一种情况，则将组合c转化为字符串并加入res
            if x == len(c) - 1:
                res.append(''.join(c))
                return
            # 递推：初始化一个Set用于排除重复字符;将第x位字符与[x,len(c)]中字符i分别交换，并进入下一层递归
            dic = set()
            for i in range(x, len(c)):
                # 1.剪枝:若c[i]在Set中，代表重复，剪枝
                if c[i] in dic:
                    continue
                # 2.将c[i]加入Set
                dic.add(c[i])
                # 3.固定c[i]为当前字符，交换c[i]和c[x]
                c[i], c[x] = c[x], c[i]
                # 4.开启下层递归：调用dfs(x+1)
                dfs(x + 1)
                # 5.还原交换:交换c[i],c[x]
                c[i], c[x] = c[x], c[i]

        dfs(0)
        return res
# leetcode submit region end(Prohibit modification and deletion)
