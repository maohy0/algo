class myQueue:
    def __init__(self):
        # 用栈实现队列的功能，需要2个栈，一个输入，一个输出
        self.stack_in = []
        self.stack_out = []

    # 将元素 x 推到队列的末尾
    def push(self, x: int) -> None:
        self.stack_in.append(x)

    # 从队列的开头移除并返回元素
    def pop(self) -> int:
        if self.empty():
            return None

        if self.stack_out:
            return self.stack_out.pop()
        else:
            for _ in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()

    # 返回队列开头的元素
    def peek(self) -> int:
        ans = self.pop()
        self.stack_out.append(ans)
        return ans

    def empty(self) -> bool:
        return not (self.stack_in or self.stack_out)