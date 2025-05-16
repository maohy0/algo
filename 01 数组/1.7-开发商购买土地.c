#include <stdio.h>
#include <stdlib.h>

void main()
{
    int n = 0, m = 0;
    scanf("%d%d", &n, &m);

    // 分别定义行、列数组
    int *r = (int *)malloc(n * sizeof(int));
    int *c = (int *)malloc(m * sizeof(int));

    // 初始化r和c
    for(int i = 0; i < n; ++i)
    {
        r[i] = 0;
    }
    for(int i = 0; i < m; ++i)
    {
        c[i] = 0;
    }

    for(int i = 0; i < n; ++i)
    {
        for(int j = 0; j < m; ++j)
        {
            int input;
            scanf("%d", &input);
            r[i] += input;  // 每一行的和
            c[j] += input;  // 每一列的和
        }
    }

    // 跟1.6类似，计算前缀和
    for(int i = 1; i < n; ++i)
    {
        r[i] += r[i - 1];
    }
    for(int i = 1; i < m; ++i)
    {
        c[i] += c[i - 1];
    }

    // 初始化为最大可能值
    int ret_hor = r[n - 1];
    int ret_ver = c[m - 1];

    // 计算按行划分的最小差异
    int ret2 = 0;
    while(ret2 < n)
    {
        ret_hor = (ret_hor > abs(r[n - 1] - 2 * r[ret2])) ? abs(r[n - 1] - 2 * r[ret2]): ret_hor;
        ++ret2;
    }

    // 计算按行划分的最小差异
    int ret1 = 0;
    while(ret1 < m)
    {
        ret_ver = (ret_ver > abs(c[m - 1] - 2 * c[ret1])) ? abs(c[m - 1] - 2 * c[ret1]): ret_ver;
        ++ret1;
    }

    printf("%d\n", (ret_ver <= ret_hor) ? ret_ver : ret_hor);   // 输出最小差距

    free(r);
    free(c);
}