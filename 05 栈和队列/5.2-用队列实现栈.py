from collections import deque

class myStack:
    def __init__(self):
        # deque是双向队列，可以用appendleft从左边添加元素，也可以用popleft从左边删除元素并返回
        self.queue_in = deque()
        self.queue_out = deque()

    # 将元素 x 压入栈顶
    def push(self, x: int) -> None:
        self.queue_in.append(x)

    # 移除并返回栈顶元素
    def pop(self) -> int:
        if self.empty():
            return None

        # 这个for循环，把queue_in除了最后一个元素，都加到了queue_out的右边，执行完之后queue_in只剩最后一个元素
        for _ in range(len(self.queue_in) - 1):
            self.queue_out.append(self.queue_in.popleft())

        self.queue_in, self.queue_out = self.queue_out, self.queue_in   # 交换queue_in和out，只有in存数据
        return self.queue_out.popleft()

    # 返回栈顶元素
    def top(self) -> int:
        if self.empty():
            return None

        return self.queue_in[-1]

    def empty(self) -> bool:
        return len(self.queue_in) == 0   # 只有 queue_in 存了数据