# include <stdio.h>
# include <stdlib.h>
# include <string.h>
# include "AQueue.h"


void InitAQueue(AQueue *Q)  //初始化队列
{

    Q->front = Q->rear = Q->length = 0;

    printf("Initialization successful\n");
}


void DestoryAQueue(AQueue *Q)   //销毁队列
{
    while(Q->front != Q->rear)
    {
        free(Q->data[Q->front]);
        Q->front = (Q->front+1)%MAXQUEUE;
    }
    free(Q->data);
    free(Q->type);
    free(Q);

    printf("Successful destruction\n");

}


Status IsFullAQueue(const AQueue *Q)    //判满
{
    if(Q->front == (Q->rear+1)%MAXQUEUE)
        return TRUE;
    return FALSE;
}


Status IsEmptyAQueue(const AQueue *Q)   //判空
{
    if(Q->front == Q->rear)
        return TRUE;
    return FALSE;
}


Status GetHeadAQueue(AQueue *Q, void *e)    //获取队首元素
{

    if(IsEmptyAQueue(Q))
    {
        printf("Empty queue.");
        return FALSE;
    }

    char type = Q->type[Q->front];

    e = GetData(Q->data[Q->front],type);

    return TRUE;
}


int LengthAQueue(AQueue *Q) //获取队列长度
{
    return Q->length;
}


Status EnAQueue(AQueue *Q, void *data,char type)  //入队操作
{
    if(IsFullAQueue(Q))    // 判满
    {
        printf("Queue full.\n");
        return FALSE;
    }

    switch(type)
    {
        case 'I':memcpy(Q->data[Q->rear],data,sizeof(int));break;
        case 'F':memcpy(Q->data[Q->rear],data,sizeof(float));break;
        case 'C':
        case 'S':memcpy(Q->data[Q->rear],data,sizeof(char*));break;
    }

    Q->rear = (Q->rear+1) % MAXQUEUE;
    Q->length++;

    return TRUE;

}


Status DeAQueue(AQueue *Q)//出队操作
{
    if(IsEmptyAQueue(Q))        //判空
    {
        printf("Empty queue,remove failed.\n");
        return FALSE;
    }

    Q->data[Q->front] = NULL;
    Q->type[Q->front] = '\0';

    Q->front = (Q->front+1)%MAXQUEUE;
    Q->length--;
    return TRUE;
}


void ClearAQueue(AQueue *Q) //清空队列
{
    for(int i=0; i<MAXQUEUE; i++)
        Q->data[i] = NULL;
    Q->front =0 ;
    Q->rear = 0;

    printf("Empty queue successfully.\n");
}


Status TraverseAQueue(const AQueue *Q, void (*foo)(void *q))    //遍历函数操作
{
    if(Q->length==0)return 0;

    int i = Q->front;
    while(i != Q->rear)
    {
        (*foo)(Q->data[i]);
        i = (i+1) % MAXQUEUE;
    }
    return TRUE;
}

void foo(void *q)
{
    ;
}

void APrint(void *q)    //操作函数
{
    ;
}

char GetType()
{
    char type;
    char* type_menu[6] = {" ---------------","|     I:Int     |","|    F:Float    |","|   S:String    |","|     C:Char    |"," ---------------"};
    for(int i=0 ; i<6 ; i++)
        printf("%s\n",type_menu[i]);
    printf("input type(I/F/S/C):\n");
    scanf("%c",&type);
    while(getchar()!='\n')
        continue;
    while(1)
    {
        if(type == 'I')
            return 'I';
        else if(type == 'F')
            return 'F';
        else if(type == 'S')
            return 'S';
        else if(type == 'C')
            return 'C';
        else
        {
            printf("Input ERROR\n");
            printf("input type again(I/F/S/C):");
        }
        scanf("%c",&type);
        while(getchar()!='\n')
            continue;
    }
    return -1;
}

void *GetKey(char type)
{
    int *Icopy = (int *)malloc(sizeof(int));
    float *Fcopy = (float *)malloc(sizeof(float));
    char *Scopy = (char *)malloc(sizeof(char) * 20);
    printf("Please enter a value\n");
    switch (type)
    {
        case 'I':       while (1)
                        {
                            if(scanf("%d", Icopy) == 1)
                                break;
                            else
                            {
                                printf( "Input ERROR\n");
                                while(getchar() != '\n');
                            }
                        };
                        return (void *)Icopy;

        case 'F':       while (1)
                        {
                            if(scanf("%f", Fcopy) == 1)
                                break;
                            else
                            {
                                printf("Input ERROR\n");
                                while(getchar() != '\n');
                            }
                        };
                        return (void *)Fcopy;

        case 'C':

        case 'S':       while (1)
                        {
                            if (scanf("%20s",Scopy) != 1)
                            {
                                printf("Input ERROR\n");
                                continue;
                            }
                            else
                                break;
                        }
                        return (void *)Scopy;

        default:    printf("ERROR\n");
    }
    while(getchar() != '\n');
    if (type != 'I')
        free(Icopy);
    if (type != 'F')
        free(Fcopy);
    if (type != 'C' && type != 'S')
        free(Scopy);
    return -1;
}

void *GetData(void *data,char type)
{
    void *key = NULL;
    int *Icopy = (int *)malloc(sizeof(int));
    float *Fcopy = (float *)malloc(sizeof(float));
    char *Scopy = (char *)malloc(sizeof(char) * 20);

    switch (type)
    {
        case 'I':       memcpy(Icopy,data,sizeof(int));
                        key = (void *)Icopy; break;

        case 'F':       memcpy(Fcopy,data,sizeof(float));
                        key = (void *)Fcopy; break;

        case 'C':

        case 'S':       memcpy(Scopy,data,strlen((char *)data));
                        key = (void *)Scopy; break;

        default:    printf("ERROR\n");
    }
    while(getchar() != '\n');
    if (type != 'I')
        free(Icopy);
    if (type != 'F')
        free(Fcopy);
    if (type != 'C' && type != 'S')
        free(Scopy);
    return key;
}

void PrintData(void *data,char type)
{
    switch(type)
    {
        case 'I':printf("%d",*(int *)data);break;
        case 'F':printf("%f",*(float *)data);break;
        case 'C':
        case 'S':printf("%s",(char *)data);break;
    }
}
