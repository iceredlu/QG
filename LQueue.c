# include <stdio.h>
# include <stdlib.h>
# include <string.h>
# include "LQueue.h"
#define LENGTH 13

void print_menu()   //打印菜单
{
    char menu[LENGTH][70] = {
        "*****************************************",
        "**        #  LQueue ADT       #        **",
        "*****************************************",
        "**        #1.initialize       #        **",
        "**        #2.destroy          #        **",
        "**        #3.is empty?        #        **",
        "**        #4.get head element #        **",
        "**        #5.get length       #        **",
        "**        #6.enter element    #        **",
        "**        #7.depart element   #        **",
        "**        #8.empty queue      #        **",
        "**        #9.traversal func   #        **",
        "******************************************",
    };
    for(int i=0; i < LENGTH; i++)
        printf("%s\n",menu[i]);
}


void switch_operat(int choice,LQueue *L)
{
    static Status init = FALSE;

    switch(choice)
    {
        case 1:InitLQueue(L);init = TRUE;break;
        case 2:
            if(init)
                DestoryLQueue(L);
            else
                printf("please initialize first.\n");
            break;
        case 3:
            if(init)
                if(IsEmptyLQueue(L))
                    printf("empty.\n");
                else
                    printf("not empty.\n");
            else
                printf("please initialize first.\n");
            break;
        case 4:
            if(init)
            {
                void *e = (char*)malloc(sizeof(char*));
                if(GetHeadLQueue(L,e))
                    printf("successfully obtained the first element.\n");
                else
                    printf("failure.\n");
            }
            else
                printf("please initialize first.\n");
            break;
        case 5:
            if(init)
            {
                int length = LengthLQueue(L);
                printf("length:%d\n",length);
            }
            else
                printf("please initialize first.\n");
            break;
        case 6:
            if(init)
            {
                char type = GetType();  //选择类型
                void *data = GetKey(type);  //输入数据值
                if(MallocNode(L))//开辟节点
                {
                    L->rear->type = type;
                    if(EnLQueue(L,data))
                    {
                        printf("enter successful.\n");
                    }
                    else
                    printf("failure.\n");
                }
                else
                    printf("failure.\n");
            }
            else
                printf("please initialize first.\n");
            break;
        case 7:
            if(init)
                if(DeLQueue(L))
                    printf("depart successful.\n");
                else
                    printf("failure.\n");
            else
                printf("please initialize first.\n");
            break;
        case 8:
            if(init)
                ClearLQueue(L);
            else
                printf("please initialize first.\n");
            break;
        case 9:
            if(init)
            {
                if(TraverseLQueue(L, LPrint))
                    printf("Complete traversal.\n");
            }
            else
                printf("please initialize first.\n");
            break;
    }
}

void InitLQueue(LQueue *Q)
{
    Q->front = Q->rear = (Node*)malloc(sizeof(Node));   //初始化
    Q->length = 0;

    printf("Initialization successful.\n");
}


void DestoryLQueue(LQueue *Q)
{
    while(Q->length != 0)
    {
        Node *p = Q->front;
        Q->front = Q->front->next;
        free(p);
        Q->length--;
    }
    free(Q);

    printf("destory successful.\n");
}


Status IsEmptyLQueue(const LQueue *Q)
{
    return (Q->length == 0) ? TRUE:FALSE;   //根据队列长度判空
}

Status GetHeadLQueue(LQueue *Q, void *e)    //获取队首元素
{
    if(Q->length == 0)
        return FALSE;

    char type = Q->front->type;

    switch(type)
    {
        case 'I':
            memcpy(e,Q->front->data,sizeof(int));
            if(memcmp(e,Q->front->data,sizeof(int))==0)
                return TRUE;
            break;
        case 'F':
            memcpy(e,Q->front->data,sizeof(float));
            if(memcmp(e,Q->front->data,sizeof(float))==0)
                return TRUE;
            break;
        case 'C':
        case 'S':
            memcpy(e,Q->front->data,strlen((char*)e));
            if(memcmp(e,Q->front->data,strlen((char*)Q->front->data))==0)
                return TRUE;
            break;
    }

    print_data(e,type);

    return TRUE;
}


int LengthLQueue(LQueue *Q)
{
    return Q->length;
}


Status MallocNode(LQueue *Q)
{
    Node *p = Q->rear;
    Q->rear = (Node*)malloc(sizeof(Node));
    p->next = Q->rear;
    if(Q->rear)
        return TRUE;
    return FALSE;
}

Status EnLQueue(LQueue *Q, void *data)
{
    char type = Q->rear->type;

    switch(type)
    {
        case 'I':
            memcpy(Q->rear->data,data,sizeof(int));Q->length++;
            if(memcmp(Q->rear->data,data,sizeof(int)) == 0)
                return TRUE;
            break;
        case 'F':
            memcpy(Q->rear->data,data,sizeof(float));Q->length++;
            if(memcmp(Q->rear->data,data,sizeof(float)) == 0)
                return TRUE;
            break;
        case 'C':
        case 'S':
            memcpy(Q->rear->data,data,strlen((char*)data));Q->length++;
            if(memcmp(Q->rear->data,data,strlen((char*)data)) == 0)
                return TRUE;
            break;
    }

    return FALSE;

}


Status DeLQueue(LQueue *Q)
{
    Node *p = Q->front;
    Q->front = Q->front->next;
    free(p);

    Q->length--;

    free(p->data);
    free(p);
}


void ClearLQueue(LQueue *Q)
{
    Node *p = Q->front;
    while(Q->front->next)
    {
        Q->front = Q->front->next;
        free(p);
        p = Q->front;
        Q->length--;
    }
    free(Q->front);
}


Status TraverseLQueue(const LQueue *Q, void (*foo)(void *q,char type))
{
    int len = Q->length;
    Node *p = Q->front;
    while(len--)
    {
        foo(p->data,p->type);
        p = p->next;
    }

    if(len == 0)
        return TRUE;
    else
        return FALSE;
}


void LPrint(void *q,char type)
{
    print_data(q,type);
}


char GetType()
{
    char *type_menu[6] = {
    "-----------------",
    "|     I.int     |",
    "|     C.char    |",
    "|     S.string  |",
    "|     F.float   |",
    "-----------------"};
    for(int i=0; i<6; i++)
        printf("%s\n",type_menu[i]);

    char types[4] = {'I','C','S','F'};
    char type;

    while(1)
    {
        printf("choice type(enter I/C/S/F):");
        scanf("%c",&type);
        while(getchar() != '\n')
            continue;
        for(int i=0; i<4; i++)
        {
            if(types[i] == type)
                return type;
        }
    }
}


void *GetKey(char type)
{
    void *key = NULL;
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
                                printf("Input ERROR\n");
                                while(getchar() != '\n');
                            }
                        };
                        key = (void *)Icopy; break;

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
                        key = (void *)Fcopy; break;

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


void print_data(void*e,char type)
{
    switch(type)
    {
        case 'I':
            printf("%d",*(int*)e);
            break;
        case 'F':
            printf("%f",*(float*)e);
            break;
        case 'C':
        case 'D':
            printf("%s",(char*)e);
            break;
    }
}




