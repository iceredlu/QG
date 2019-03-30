#include <stdio.h>
#include <stdlib.h>
#include "LinkStack.h"

int main()
{
    int choice;

    char menu[12][50] = {
        "************************************",
        "**        #   ��ջ        #       **",
        "************************************",
        "**        #1.��ջ��ʼ��   #       **",
        "**        #2.�ж�ջ��     #       **",
        "**        #3.�õ�ջ��Ԫ�� #       **",
        "**        #4.���ջ       #       **",
        "**        #5.����ջ       #       **",
        "**        #6.���ջ����   #       **",
        "**        #7.��ջ         #       **",
        "**        #8.��ջ         #       **",
        "************************************",
    };

    LinkStack LS;

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
                if(initLStack(&LS)==SUCCESS)
                {
                    printf("��ʼ���ɹ���\n");
                    init = initLStack(&LS);
                }
                else
                    printf("��ʼ��ʧ�ܡ�\n");
                break;
            case 2:
                if(init == SUCCESS)
                    if(isEmptyLStack(&LS))
                        printf("ջ�ա�\n");
                    else printf("ջ��Ϊ�ա�\n");
                else
                    printf("δ���г�ʼ�������������롣\n");
                break;
            case 3:
                if(init == SUCCESS)
                {
                    ElemType e;
                    if(getTopLStack(&LS,&e))
                        printf("ջ��Ԫ�أ�%d\n",e);
                    else
                        printf("��ȡջ��Ԫ��ʧ�ܡ�\n");
                }
                else
                    printf("δ���г�ʼ�������������롣\n");
                break;
            case 4:
                if(init == SUCCESS){
                    if(clearLStack(&LS))
                        printf("���ջ�ɹ���\n");
                    else
                        printf("���ʧ�ܡ�\n");
                }
                else
                    printf("δ���г�ʼ�������������롣\n");
                break;
            case 5:
                if(init == SUCCESS)
                    if(destroyLStack(&LS))
                        printf("����ջ�ɹ���\n");
                    else
                        printf("����ջʧ�ܡ�\n");
                else
                    printf("δ���г�ʼ�������������롣\n");
                break;
            case 6:
                if(init == SUCCESS)
                {
                    int length;//��ַ��Ϊ�βδ���LStackLength�õ�����
                    if(LStackLength(&LS,&length))
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
                    while(getchar()!='\n')
                        continue;
                    if(pushLStack(&LS,data))
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
                    ElemType data;//��ַ��Ϊ�βδ���popLStack��ȡ��ջ����
                    if(popLStack(&LS,&data))
                        printf("��ջ���ݣ�%d\n",data);
                    else
                        printf("��ջʧ�ܡ�\n");
                }
                else
                    printf("δ���г�ʼ�������������롣\n");
                break;
        }

        printf("���������<1-8>������0�˳���:");
        scanf("%d",&choice);

        while(getchar() != '\n')
            continue;
    }

    printf("Done.");

    return 0;

}
