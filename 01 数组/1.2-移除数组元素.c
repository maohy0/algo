#include <stdio.h>

int RemoveElement(int* nums, int numslen, int val)
{
    // 用2个指针来操作数组，两边夹，删除数组并不简单，因为数组的内存空间是连续的，需要删除后循环迭代
    int slow = 0;
    int fast = 0;
    for(;fast<numslen;++fast)
    {
        // 如果指向的元素等于val，则此次循环不执行任何操作，fast+1，继续向后迭代
        if(nums[fast] != val)   // 这里注意是要删除数组中所有等于val的元素
        {
            nums[slow++] = nums[fast];  // 不删除的元素直接迭代
        }
    }
    return slow;   // 返回新数组的长度
}

void main()
{
    int numslen = 0;
    int val = 0;
    printf("Please input the length of nums:\n");
    scanf("%d",&numslen);
    int nums[numslen];
    printf("Please input nums:\n");
    for(int i=0;i<numslen;++i)
    {
        scanf("%d",&nums[i]);
    }
    printf("Please input val:\n");
    scanf("%d",&val);
    int newlength;
    newlength = RemoveElement(nums,numslen,val);
    printf("Length of new nums: %d\n",newlength);
    printf("new nums:\n");
    for(int i=0;i<newlength;++i)
    {
        printf("%d\t",nums[i]);
    }
}
