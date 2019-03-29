# include <stdlib.h>
# include <stdio.h>
# include "SqStack.h"

//˳��ջ(���������)
Status initStack(SqStack *s,int sizes)  //��ʼ��ջ
{
    s->elem = (ElemType*)malloc(sizes * sizeof(ElemType));//����ջ�Ŀռ�
    if(s->elem) //�ж�s->elem�Ƿ�ɹ�����ռ�
    {
        s->top = -1;
        s->size = sizes;
        return SUCCESS;//Ϊ��ʱ���ó�ʼ������������SUCCESS��֪��ʼ���ɹ�
    }
   else return ERROR;//��ʼ��ʧ�ܡ�
}

Status isEmptyStack(SqStack *s)  //�ж�ջ�Ƿ�Ϊ��
{
    if(s->top == -1)
        return SUCCESS;
    else
        return ERROR;
}

Status getTopStack(SqStack *s,ElemType *e)  //�õ�ջ��Ԫ��
{
    if(s->top == -1)//�ж�ջ�գ��ǿս�ջ������ָ�����e
        return ERROR;
    *e = s->elem[s->top];
}

Status clearStack(SqStack *s)  //���ջ
{
    if(s->elem != NULL)
    {s->top = -1;
    return SUCCESS;}
    return ERROR;
}

Status destroyStack(SqStack *s) //����ջ
{
    free(s->elem);//free������ݵ�����
    s->size = 0;
    s->top = -1;
    return SUCCESS;
}

Status stackLength(SqStack *s,int *length)  //���ջ����
{
    *length = s->top+1;
}

Status pushStack(SqStack *s,ElemType data) //��ջ
{
    if(s->top >= s->size-1)//�ж�ջ�Ƿ�����
        return ERROR;
    s->top++;//ջ������
    s->elem[s->top] = data;
    return SUCCESS;
}

Status popStack(SqStack *s,ElemType *data)  //��ջ
{
    if(s->top == -1)    //�ж�ջ��
        return ERROR;
    *data = s->elem[s->top];//����ս���ݸ�ֵ��ָ�����
    s->top--;//ջ������
    return SUCCESS;

}

