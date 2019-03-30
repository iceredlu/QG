#include <stdio.h>
#include <stdlib.h>
#include "LinkStack.h"

int main()
{
    int choice;

    char menu[12][50] = {
        "************************************",
        "**        #   链栈        #       **",
        "************************************",
        "**        #1.链栈初始化   #       **",
        "**        #2.判断栈空     #       **",
        "**        #3.得到栈顶元素 #       **",
        "**        #4.清空栈       #       **",
        "**        #5.销毁栈       #       **",
        "**        #6.检测栈长度   #       **",
        "**        #7.入栈         #       **",
        "**        #8.出栈         #       **",
        "************************************",
    };

    LinkStack LS;

    Status init = ERROR;//用于判断是否已初始化

    int i;
    for(i =0;i < 12;i++)
        printf("%s\n",menu[i]);
    puts("请输入操作数<1-8>:");
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
                    printf("初始化成功。\n");
                    init = initLStack(&LS);
                }
                else
                    printf("初始化失败。\n");
                break;
            case 2:
                if(init == SUCCESS)
                    if(isEmptyLStack(&LS))
                        printf("栈空。\n");
                    else printf("栈不为空。\n");
                else
                    printf("未进行初始化，请重新输入。\n");
                break;
            case 3:
                if(init == SUCCESS)
                {
                    ElemType e;
                    if(getTopLStack(&LS,&e))
                        printf("栈顶元素：%d\n",e);
                    else
                        printf("获取栈顶元素失败。\n");
                }
                else
                    printf("未进行初始化，请重新输入。\n");
                break;
            case 4:
                if(init == SUCCESS){
                    if(clearLStack(&LS))
                        printf("清空栈成功。\n");
                    else
                        printf("清空失败。\n");
                }
                else
                    printf("未进行初始化，请重新输入。\n");
                break;
            case 5:
                if(init == SUCCESS)
                    if(destroyLStack(&LS))
                        printf("销毁栈成功。\n");
                    else
                        printf("销毁栈失败。\n");
                else
                    printf("未进行初始化，请重新输入。\n");
                break;
            case 6:
                if(init == SUCCESS)
                {
                    int length;//地址作为形参传入LStackLength得到长度
                    if(LStackLength(&LS,&length))
                        printf("栈长:%d\n",length);
                    else
                        printf("获取栈长失败。\n");
                }
                else
                    printf("未进行初始化，请重新输入。\n");
                break;
            case 7:
                if(init == SUCCESS)
                {
                    ElemType data;
                    puts("请输入入栈数据：");
                    scanf("%d",&data);
                    while(getchar()!='\n')
                        continue;
                    if(pushLStack(&LS,data))
                        printf("入栈成功。\n");
                    else
                        printf("入栈失败。\n");
                }
                else
                    printf("未进行初始化，请重新输入。\n");
                break;
            case 8:
                if(init == SUCCESS)
                {
                    ElemType data;//地址作为形参传入popLStack读取出栈数据
                    if(popLStack(&LS,&data))
                        printf("出栈数据：%d\n",data);
                    else
                        printf("出栈失败。\n");
                }
                else
                    printf("未进行初始化，请重新输入。\n");
                break;
        }

        printf("输入操作数<1-8>（输入0退出）:");
        scanf("%d",&choice);

        while(getchar() != '\n')
            continue;
    }

    printf("Done.");

    return 0;

}
