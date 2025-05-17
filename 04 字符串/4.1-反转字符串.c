#include <stdio.h>
#include <stdlib.h>

char* reversestr(char* s, int lengthofs)
{
    int left = 0;
    int right = lengthofs - 1;

    while(left < right)
    {
        char temp = s[left];
        s[left++] = s[right];
        s[right--] = temp;
    }
    return s;
}

int main()
{
    int lengthofs = 5;
    char *s = (char *)malloc(lengthofs * sizeof(char));
    s[0] = 'h';
    s[1] = 'e';
    s[2] = 'l';
    s[3] = 'l';
    s[4] = 'o';
    s = reversestr(s, lengthofs);
    for(int i = 0; i < lengthofs; ++i)
    {
        printf("%c\t", s[i]);
    }
    printf("\n");
    return 1;
}