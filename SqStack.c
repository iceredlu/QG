# include <stdlib.h>
# include <stdio.h>
# include "SqStack.h"

//顺序栈(基于数组的)
Status initStack(SqStack *s,int sizes)  //初始化栈
{
    s->elem = (ElemType*)malloc(sizes * sizeof(ElemType));//开辟栈的空间
    if(s->elem) //判断s->elem是否成功分配空间
    {
        s->top = -1;
        s->size = sizes;
        return SUCCESS;//为空时设置初始化参数并返回SUCCESS告知初始化成功
    }
   else return ERROR;//初始化失败。
}

Status isEmptyStack(SqStack *s)  //判断栈是否为空
{
    if(s->top == -1)
        return SUCCESS;
    else
        return ERROR;
}

Status getTopStack(SqStack *s,ElemType *e)  //得到栈顶元素
{
    if(s->top == -1)//判断栈空，非空将栈顶赋给指针变量e
        return ERROR;
    *e = s->elem[s->top];
}

Status clearStack(SqStack *s)  //清空栈
{
    if(s->elem != NULL)
    {s->top = -1;
    return SUCCESS;}
    return ERROR;
}

Status destroyStack(SqStack *s) //销毁栈
{
    free(s->elem);//free存放数据的数组
    s->size = 0;
    s->top = -1;
    return SUCCESS;
}

Status stackLength(SqStack *s,int *length)  //检测栈长度
{
    *length = s->top+1;
}

Status pushStack(SqStack *s,ElemType data) //入栈
{
    if(s->top >= s->size-1)//判断栈是否已满
        return ERROR;
    s->top++;//栈顶上移
    s->elem[s->top] = data;
    return SUCCESS;
}

Status popStack(SqStack *s,ElemType *data)  //出栈
{
    if(s->top == -1)    //判断栈空
        return ERROR;
    *data = s->elem[s->top];//将出战数据赋值给指针参数
    s->top--;//栈顶下移
    return SUCCESS;

}

