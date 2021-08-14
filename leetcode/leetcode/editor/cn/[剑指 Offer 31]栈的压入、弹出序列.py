# 输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如，序列 {1,2,3,4,5} 是某栈
# 的压栈序列，序列 {4,5,3,2,1} 是该压栈序列对应的一个弹出序列，但 {4,3,5,1,2} 就不可能是该压栈序列的弹出序列。 
# 
#  
# 
#  示例 1： 
# 
#  输入：pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
# 输出：true
# 解释：我们可以按以下顺序执行：
# push(1), push(2), push(3), push(4), pop() -> 4,
# push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
#  
# 
#  示例 2： 
# 
#  输入：pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
# 输出：false
# 解释：1 不能在 2 之前弹出。
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= pushed.length == popped.length <= 1000 
#  0 <= pushed[i], popped[i] < 1000 
#  pushed 是 popped 的排列。 
#  
# 
#  注意：本题与主站 946 题相同：https://leetcode-cn.com/problems/validate-stack-sequences/ 
#  Related Topics 栈 数组 模拟 
#  👍 218 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        # 初始化：辅助栈，弹出序列的索引i
        stack = []
        i = 0

        # 遍历压栈序列：各元素记为num
        for num in pushed:
            # 1.num入栈
            stack.append(num)
            # 2.循环出栈：若stack栈顶元素==popped[i]，则执行出栈与i++
            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        # 返回值：若stack为空，则此弹出序列合法
        return not stack
# leetcode submit region end(Prohibit modification and deletion)
