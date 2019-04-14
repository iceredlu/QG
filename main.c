#include <stdio.h>
#include <stdlib.h>
#include "sort.h"

int main()
{
    sort_menu();

    int method,length;//排序方式，数组长度

    while(1)
    {
        printf("enter array length:");
        scanf("%d",&length);

        int a[length];

        printf("enter array:");

        for(int i=0; i < length; i++)
        {
            scanf("%d",&a[i]);
        }

        while(getchar()!='\n')
            continue;

        printf("choose sorting method:");
        if(scanf("%d",&method) && method>0 && method <10)
        {
            while(getchar() != '\n');
            sort_method(method,a,length);
        }
        else
            printf("worong enter.\n\n");

        printf("enter any key to continue,0 to quit.\n");

        if(getchar() == 48)
            break;
    }


    return 0;
}

