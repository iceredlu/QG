#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "AQueue.h"
#define LENGTH 15

int main()
{
    char menu[LENGTH][70] = {
        "***************************************************",
        "**        #    Circular Queue ADT       #        **",
        "***************************************************",
        "**        #1.Initialization queue       #        **",
        "**        #2.Destroy queue              #        **",
        "**        #3.Check if the queue is full #        **",
        "**        #4.Check if the queue is empty#        **",
        "**        #5.View queue head elements   #        **",
        "**        #6.Determine queue length     #        **",
        "**        #7.Insert element             #        **",
        "**        #8.Departure                  #        **",
        "**        #9.Empty queue                #        **",
        "**        #10.Traversal function        #        **",
        "**        #11.Operation function        #        **",
        "***************************************************"
    };
    for(int i=0; i < LENGTH; i++)
        printf("%s\n",menu[i]);

    AQueue Aqueue;
    int choice;

    Status init = FALSE;    //用于判断是否初始化

    puts("Input operand:");

    while(scanf("%d",&choice) && choice>0 && choice <=11)
    {
        switch(choice)
        {
        case 1:
            InitAQueue(&Aqueue);
            init = TRUE;
            break;
        case 2:
            if(init)
                DestoryAQueue(&Aqueue);
            else
                puts("The queue has not been initialized, please initialize it first.\n");
            break;
        case 3:
            if(init)
                if(IsFullAQueue(&Aqueue))
                    puts("Full.");
                else
                    puts("Not full.");
            else
                puts("The queue has not been initialized, please initialize it first.\n");
            break;
        case 4:
            if(init)
                if(IsEmptyAQueue(&Aqueue))
                    puts("Empty.");
                else
                    puts("Not empty.");
            else
                puts("The queue has not been initialized, please initialize it first.\n");
            break;
        case 5:
            if(init)
            {
                void *e;
                if(GetHeadAQueue(&Aqueue,e))
                    PrintData(e,Aqueue.type[Aqueue.front]);
                else
                    printf("get head aqueue failure.\n");
            }
            else
                puts("The queue has not been initialized, please initialize it first.\n");
            break;
        case 6:
            if(init)
            {
                int length = LengthAQueue(&Aqueue);
                printf("Queue length:%d\n",length);
            }
            else
                puts("The queue has not been initialized, please initialize it first.\n");
            break;
        case 7:
            if(init)
            {
                void *data;
                char type = GetType();      //选择数据类型
                data = GetKey(type);        //输入入队数据
                if(EnAQueue(&Aqueue,data,type))      //入队操作
                    PrintData(data,type);
                else
                    printf("Entry failure.\n");
            }
            else
                puts("The queue has not been initialized, please initialize it first.\n");
            break;
        case 8:
            if(init)
                if(DeAQueue(&Aqueue))
                    printf("Departure successful.\n");
                else
                    printf("Departure failure.\n");
            else
                puts("The queue has not been initialized, please initialize it first.\n");
            break;
        case 9:
            if(init)
                ClearAQueue(&Aqueue);
            else
                puts("The queue has not been initialized, please initialize it first.\n");
            break;
        case 10:
            if(init)
                if(TraverseAQueue(&Aqueue,foo))
                    printf("Traverse successful.\n");
                else
                    printf("Traverse failure.\n");
            else
                puts("The queue has not been initialized, please initialize it first.\n");
            break;
        case 11:
            if(init){
                void *data;
                char type = GetType();      //选择数据类型
                data = GetKey(type);
                APrint(data);}
            else
                puts("The queue has not been initialized, please initialize it first.\n");
            break;
        }
    printf("Input operand(0 to qiut):");
    }


    return 0;
}

