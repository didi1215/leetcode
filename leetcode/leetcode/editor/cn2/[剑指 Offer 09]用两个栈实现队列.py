# 用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的
# 功能。(若队列中没有元素，deleteHead 操作返回 -1 ) 
# 
#  
# 
#  示例 1： 
# 
#  输入：
# ["CQueue","appendTail","deleteHead","deleteHead"]
# [[],[3],[],[]]
# 输出：[null,null,3,-1]
#  
# 
#  示例 2： 
# 
#  输入：
# ["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
# [[],[],[5],[2],[],[]]
# 输出：[null,-1,null,null,5,2]
#  
# 
#  提示： 
# 
#  
#  1 <= values <= 10000 
#  最多会对 appendTail、deleteHead 进行 10000 次调用 
#  
#  Related Topics 栈 设计 队列 
#  👍 273 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class CQueue:
    # 只使用一个栈 stack1 当作队列，另一个栈 stack2 用来辅助操作。

    # 要想将新加入的元素出现栈底，需要先将 stack1 的元素转移到 stack2，
    # 将元素入栈 stack1，最后将 stack2 的元素全部回到 stack1。

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, value: int) -> None:
        # 当stack1中有数，把它pop出添加到stack2
        # 1->2
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        # value加入stack1
        self.stack1.append(value)
        # 2->1
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return self.stack1

    def deleteHead(self) -> int:
        if not self.stack1:
            return -1
        return self.stack1.pop()

# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
# leetcode submit region end(Prohibit modification and deletion)
