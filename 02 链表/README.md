# 02 链表 Chain Table

链表和数组不同，它不一定是同一类型的数据组成，而且在内存的空间不连续。

链表的每个节点分为2部分，一部分为数据部分，另一部分存放指向下一元素的指针，最后一个节点指向的指针为NULL（空指针）

链表可以分为3类：

## 单链表
刚刚说的就是单链表

## 双链表
每一个节点一前一后有2个指针，一个指向上一个节点，一个指向下一个

## 循环链表
顾名思义，链表首尾相连，最后一个节点的指针指向第一个元素