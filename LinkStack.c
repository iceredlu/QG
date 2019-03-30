# include <stdio.h>
# include <stdlib.h>
# include "LinkStack.h"

//链栈(基于链表的)
Status initLStack(LinkStack *s)   //初始化
{
    //top指针指向栈顶元素的上一个位置
    s->top = (LinkStackPtr)malloc(sizeof(StackNode));//为top分配内存空间
    if(s->top)
    {
        s->top->next = NULL;//初始化时next指向空指针，栈元素个数为零
        s->count = 0;
        return SUCCESS;
    }
    return ERROR;
}

Status isEmptyLStack(LinkStack *s)  //判断链栈是否为空
{
    if(s->top->next == NULL && s->count == 0)   //栈顶指向空指针且栈元素个数为0时栈空。
        return SUCCESS;
    return ERROR;
}

Status getTopLStack(LinkStack *s,ElemType *e)  //得到栈顶元素
{
    if(s->top->next == NULL)    //判断栈空
        return ERROR;
    *e = s->top->data;  //栈顶赋值给指针参数
    return SUCCESS;
}

Status clearLStack(LinkStack *s)   //清空栈
{
    LinkStackPtr p;
    while(s->top) {  //s->top存放在p中，s->top下移，释放p，直到s->top为空指针。    {
        p = s->top;
        s->top = s->top->next;
        free(p);
    }
    s->count = 0;
    return SUCCESS;
}

Status destroyLStack(LinkStack *s)   //销毁栈
{
    if(!s->top) //判断栈空
        return ERROR;

    clearLStack(s);     //清空链栈
    free(s);        //释放结构栈
    return SUCCESS;
}

Status LStackLength(LinkStack *s,int *length)    //检测栈长度
{
    if(s->top == NULL)
    {
        printf("链栈被销毁。");
        return ERROR;
    }
    *length = s->count;

    return SUCCESS;
}

Status pushLStack(LinkStack *s,ElemType data)   //入栈
{
    if(s->top == NULL)
        return ERROR;
    LinkStackPtr p = (LinkStackPtr)malloc(sizeof(StackNode));//开辟新节点存放数据
    p->next = s->top;   //新节点的next指向top，top上移。
    s->top = p;
    p->data = data;
    s->count++;

    return SUCCESS;
}

Status popLStack(LinkStack *s,ElemType *data)   //出栈
{
    if(s->count == 0)//判断栈空
        return ERROR;

    *data = s->top->data;   //将出战的值赋给指针参数
    LinkStackPtr p = s->top;    //p指向top，top指向下一个，释放p，出栈完成。
    s->top = p->next;
    free(p);
    s->count--;

    return SUCCESS;
}
