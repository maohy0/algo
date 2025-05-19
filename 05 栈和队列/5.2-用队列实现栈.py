from collections import deque

class myStack:
    def __init__(self):
        # deque是双向队列，可以用appendleft从左边添加元素，也可以用popleft从左边删除元素并返回
        self.q = deque()

    # 将元素 x 压入栈顶
    def push(self, x: int) -> None:
        self.q.append(x)

    # 移除并返回栈顶元素
    def pop(self) -> int:
        if self.empty():
            return None

        # 这个for循环，把queue_in除了最后一个元素，都加到了queue_out的右边，执行完之后queue_in只剩最后一个元素
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

        return self.q.popleft()

    # 返回栈顶元素
    def top(self) -> int:
        if self.empty():
            return None

        return self.q[-1]

    def empty(self) -> bool:
        return len(self.q) == 0   # 只有 queue_in 存了数据