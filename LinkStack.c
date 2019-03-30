# include <stdio.h>
# include <stdlib.h>
# include "LinkStack.h"

//��ջ(���������)
Status initLStack(LinkStack *s)   //��ʼ��
{
    //topָ��ָ��ջ��Ԫ�ص���һ��λ��
    s->top = (LinkStackPtr)malloc(sizeof(StackNode));//Ϊtop�����ڴ�ռ�
    if(s->top)
    {
        s->top->next = NULL;//��ʼ��ʱnextָ���ָ�룬ջԪ�ظ���Ϊ��
        s->count = 0;
        return SUCCESS;
    }
    return ERROR;
}

Status isEmptyLStack(LinkStack *s)  //�ж���ջ�Ƿ�Ϊ��
{
    if(s->top->next == NULL && s->count == 0)   //ջ��ָ���ָ����ջԪ�ظ���Ϊ0ʱջ�ա�
        return SUCCESS;
    return ERROR;
}

Status getTopLStack(LinkStack *s,ElemType *e)  //�õ�ջ��Ԫ��
{
    if(s->top->next == NULL)    //�ж�ջ��
        return ERROR;
    *e = s->top->data;  //ջ����ֵ��ָ�����
    return SUCCESS;
}

Status clearLStack(LinkStack *s)   //���ջ
{
    LinkStackPtr p;
    while(s->top) {  //s->top�����p�У�s->top���ƣ��ͷ�p��ֱ��s->topΪ��ָ�롣    {
        p = s->top;
        s->top = s->top->next;
        free(p);
    }
    s->count = 0;
    return SUCCESS;
}

Status destroyLStack(LinkStack *s)   //����ջ
{
    if(!s->top) //�ж�ջ��
        return ERROR;

    clearLStack(s);     //�����ջ
    free(s);        //�ͷŽṹջ
    return SUCCESS;
}

Status LStackLength(LinkStack *s,int *length)    //���ջ����
{
    if(s->top == NULL)
    {
        printf("��ջ�����١�");
        return ERROR;
    }
    *length = s->count;

    return SUCCESS;
}

Status pushLStack(LinkStack *s,ElemType data)   //��ջ
{
    if(s->top == NULL)
        return ERROR;
    LinkStackPtr p = (LinkStackPtr)malloc(sizeof(StackNode));//�����½ڵ�������
    p->next = s->top;   //�½ڵ��nextָ��top��top���ơ�
    s->top = p;
    p->data = data;
    s->count++;

    return SUCCESS;
}

Status popLStack(LinkStack *s,ElemType *data)   //��ջ
{
    if(s->count == 0)//�ж�ջ��
        return ERROR;

    *data = s->top->data;   //����ս��ֵ����ָ�����
    LinkStackPtr p = s->top;    //pָ��top��topָ����һ�����ͷ�p����ջ��ɡ�
    s->top = p->next;
    free(p);
    s->count--;

    return SUCCESS;
}
