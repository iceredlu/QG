#include <stdio.h>
#include <stdlib.h>
#include "SqStack.h"

int main()
{
    int choice;

    char menu[12][50] = {
        "******************************************",
        "**          # ���������˳��ջ  #       **",
        "******************************************",
        "**          #1.��ʼ��ջ         #       **",
        "**          #2.�ж�ջ��         #       **",
        "**          #3.�õ�ջ��Ԫ��     #       **",
        "**          #4.���ջ           #       **",
        "**          #5.����ջ           #       **",
        "**          #6.���ջ����       #       **",
        "**          #7.��ջ             #       **",
        "**          #8.��ջ             #       **",
        "******************************************",
    };

    SqStack sqstack;
    int size;   //����ջ��ָ����С

    puts("������ջ�����ռ䣺");
    scanf("%d",&size);

    Status init = ERROR;//�����ж��Ƿ��ѳ�ʼ��

    int i;
    for(i =0;i < 12;i++)
        printf("%s\n",menu[i]);
    puts("�����������<1-8>:");
    scanf("%d",&choice);
    while(getchar()!= '\n')
        continue;
    while(choice>0 && choice <=8)
    {
        switch(choice)
        {
            case 1:
                if(initStack(&sqstack,size)==SUCCESS)
                {
                    printf("��ʼ���ɹ���\n");
                    init = initStack(&sqstack,size);
                }
                else
                    printf("��ʼ��ʧ�ܡ�\n");
                break;
            case 2:
                if(init == SUCCESS)
                    if(isEmptyStack(&sqstack))
                        printf("ջ�ա�\n");
                    else printf("ջ��Ϊ�ա�\n");
                else
                    printf("δ���г�ʼ�������������롣\n");
                break;
            case 3:
                if(init == SUCCESS)
                {
                    ElemType e;
                    if(getTopStack(&sqstack,&e))
                        printf("ջ��Ԫ�أ�%d\n",e);
                    else
                        printf("��ȡջ��Ԫ��ʧ�ܡ�\n");
                }
                else
                    printf("δ���г�ʼ�������������롣\n");
                break;
            case 4:
                if(init == SUCCESS){
                    if(clearStack(&sqstack))
                        printf("���ջ�ɹ���\n");
                    else
                        printf("���ʧ�ܡ�\n");
                }
                else
                    printf("δ���г�ʼ�������������롣\n");
                break;
            case 5:
                if(init == SUCCESS)
                    if(destroyStack(&sqstack))
                        printf("����ջ�ɹ���\n");
                    else
                        printf("����ջʧ�ܡ�\n");
                else
                    printf("δ���г�ʼ�������������롣\n");
                break;
            case 6:
                if(init == SUCCESS)
                {
                    int length;
                    if(stackLength(&sqstack,&length))
                        printf("ջ��:%d\n",length);
                    else
                        printf("��ȡջ��ʧ�ܡ�\n");
                }
                else
                    printf("δ���г�ʼ�������������롣\n");
                break;
            case 7:
                if(init == SUCCESS)
                {
                    ElemType data;
                    puts("��������ջ���ݣ�");
                    scanf("%d",&data);
                    if(pushStack(&sqstack,data))
                        printf("��ջ�ɹ���\n");
                    else
                        printf("��ջʧ�ܡ�\n");
                }
                else
                    printf("δ���г�ʼ�������������롣\n");
                break;
            case 8:
                if(init == SUCCESS)
                {
                    ElemType data;
                    if(popStack(&sqstack,&data))
                        printf("��ջ���ݣ�%d\n",data);
                    else
                        printf("��ջʧ�ܡ�\n");
                }
                else
                    printf("δ���г�ʼ�������������롣\n");
                break;
        }

        printf("���������<1-8>������q�˳���:");
        scanf("%d",&choice);

        while(getchar() != '\n')
            continue;
    }

    printf("Done.");

    return 0;
}
