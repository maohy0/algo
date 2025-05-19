#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct{
    int stack_in_top, stack_out_top;    // stack_in_top和stack_out_top指向栈顶
    int stack_in[100], stack_out[100];
} myQueue;

// 用栈实现队列的功能，需要2个栈，一个输入，一个输出
myQueue* createQueue(){
    myQueue* queue = (myQueue *)malloc(sizeof(myQueue));
    queue -> stack_in_top = 0;
    queue -> stack_out_top = 0;
    return queue;
}

// 将元素 x 推到队列的末尾
void push(myQueue* obj, int x){
    obj -> stack_in[(obj -> stack_in_top)++] = x;   // 先将 x 存入栈顶指针中，然后栈顶指针+1
}

// 从队列的开头移除并返回元素
int pop(myQueue* obj){
    // 复制栈顶指针，减少访问内存的次数
    int stack_in_top = obj -> stack_in_top;
    int stack_out_top = obj -> stack_out_top;
    // 输出栈为空
    if(stack_out_top == 0)
    {
        while(stack_in_top > 0)
        {
            obj -> stack_out[stack_out_top++] = obj -> stack_in[--stack_in_top];    // 把输入栈的元素复制到输出栈中，倒着进栈，这样开头就在栈顶了
        }
    }
    int top = obj -> stack_out[--stack_out_top];    // 保存输出栈的栈顶指针，栈顶指针就等于栈的长度，比元素高1
    while(stack_out_top > 0)
    {
        obj -> stack_in[stack_in_top++] = obj->stack_out[--stack_out_top];  // 把输出栈元素更新回输入栈中
    }
    // 更新栈顶指针
    obj -> stack_in_top = stack_in_top;
    obj -> stack_out_top = stack_out_top;
    return top;
}

// 返回队列开头的元素
int peek(myQueue* obj){
    return obj -> stack_in[0];  // 输入栈中的栈底元素
}

bool empty(myQueue* obj){
    return obj -> stack_in_top == 0 && obj -> stack_out_top == 0;
}

void freeQueue(myQueue* obj){
    obj -> stack_in_top = 0;
    obj -> stack_out_top = 0;
    free(obj);
}