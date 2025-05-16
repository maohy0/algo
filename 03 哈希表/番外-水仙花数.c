#include <stdio.h>
#include <stdbool.h>
#include <math.h>

// 跟python不同，c原生支持的函数不够丰富，繁琐一些，c不支持直接把数转为字符串，所以用到循环较多
bool is_narcissistic(int num)
{
    int n = 0;
    int new_sum = 0;

    // 计算位数n
    int temp = n;
    while(temp != 0)
    {
        temp /= 10;
        ++n;
    }

    temp = num;
    while(temp != 0)
    {
        int digit = temp % 10;  // 取余数，最后一位
        new_sum += (int)pow(digit, n);
        temp /= 10;
    }
    if(new_sum == num)
    {
        return true;
    }
    else{
        return false;
    }
}

void main()
{
    printf("%d\n", is_narcissistic(153));
}