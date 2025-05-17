#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* reversestr2(char* s, int k)
{
    for(int i = 0; i < strlen(s); i += 2 * k)
    {
        k = i + k > strlen(s) ? strlen(s) - i: k;

        int left = i;
        int right = i + k - 1;
        while(left < right)
        {
            char temp = s[left];
            s[left++] = s[right];
            s[right--] = temp;
        }
    }
    return s;
}

void main()
{
    char *s = (char *)malloc(8 * sizeof(char)); // 多分配一位，因为字符串结尾的'\0'，否则会出warning，程序可能无法运行
    strcpy(s, "abcdefg");
    puts(reversestr2(s, 2));
    free(s);
}