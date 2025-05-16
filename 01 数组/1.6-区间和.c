#include <stdio.h>
#include <stdlib.h>

void main()
{
    int n;    // 数组长度
    scanf("%d", &n);

    // 使用动态内存分配，而不用静态数组
    int *a = (int *)malloc((n + 1) * sizeof(int));
    
    a[0] = 0;   // 此处注意，输入的数组和存储的数组a不一样，是通过累加的方式存储的，所以malloc申请 n+1 个空间

    for(int i = 1; i <= n; ++i)
    {
        int j;
        scanf("%d", &j);
        a[i] = a[i - 1] + j;
    }

    int left, right;

    while(scanf("%d%d", &left, &right) == 2)    // 一个很有趣的知识点，scanf是有返回值的，返回成功匹配并赋值的个数
    {
        printf("%d\n", a[right + 1] - a[left]);
    }

    free(a);
}