#include <stdio.h>
#include <stdlib.h>
#include "text.h"

int main()
{

    int length;

    int choice;
    printf("\ttext\n");
    printf("1,text large amount of data\n");
    printf("2.text a large number of small arrays\n");
    printf("enter your choice:");

    scanf("%d",&choice);

    while(choice)
    {
        switch(choice)
        {
            case 1:
                {
                        printf("Select data volume:");

                        while(scanf("%d",&length))
                        {

                            int a[length];

                            printf("When the amount of data is %d:\n",length);

                            insertSort(a,length);
                            saveArray(a,length);

                            text_amount(a,length);

                            printf("Select data volume(0 to quit):");


                            if(length== 0)
                                break;

                        }
                        break;
                }
            case 2:
                {
                    printf("Each array size:");

                    while(scanf("%d",&length))
                    {
                        int a[length];

                        int num;
                        printf("small arrays number:");
                        scanf("%d",&num);

                        printf("%d arrays of length %d",num,length);

                        text_array(a,length,num);

                        printf("Each array size(0 to quit):");


                        if(length== 0)
                            break;

                    }
                    break;
                }
            default:
                printf("worong choice.\n");

        }

        printf("enter you choice again(0 to quit):");
    }



    return 0;
}
