#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* replacenumber(char *s)
{
    int length = strlen(s);
    char* result = (char*)malloc((6 * length + 1) * sizeof(char));  // 最大长度为 6 * length，加上1存储'\0'
    int j = 0;
    for(int i = 0; i < length; ++i)
    {
        if(s[i] >= '0' && s[i] <= '9')
        {
            strcat(result, "number");
            j += 6;
        }
        else if(s[i] >= 'a' && s[i] <= 'z')
        {
            result[j++] = s[i];
        }
    }
    return result;
}

void main()
{
    char *str = (char *)malloc(10000 * sizeof(char));
    gets(str);
    puts(replacenumber(str));
    free(str);
}