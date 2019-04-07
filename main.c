#include <stdio.h>
#include <stdlib.h>
#include "LQueue.h"

int main()
{
    print_menu();

    LQueue *L = (LQueue *)malloc(sizeof(LQueue));
    int choice;

    printf("Input operand:");

    while(scanf("%d",&choice) && choice>0 && choice < 10)
    {
        switch_operat(choice,L);
        printf("Input operand(0 to qiut):");
    }

    printf("done~\n");

    return 0;
}

