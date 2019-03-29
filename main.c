#include <stdio.h>
#include <stdlib.h>
#include "SqStack.h"

int main()
{
    int choice;

    char menu[12][50] = {
        "******************************************",
        "**          # 基于数组的顺序栈  #       **",
        "******************************************",
        "**          #1.初始化栈         #       **",
        "**          #2.判断栈空         #       **",
        "**          #3.得到栈顶元素     #       **",
        "**          #4.清空栈           #       **",
        "**          #5.销毁栈           #       **",
        "**          #6.检测栈长度       #       **",
        "**          #7.入栈             #       **",
        "**          #8.出栈             #       **",
        "******************************************",
    };

    SqStack sqstack;
    int size;   //创建栈并指定大小

    puts("请输入栈的最大空间：");
    scanf("%d",&size);

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
                if(initStack(&sqstack,size)==SUCCESS)
                {
                    printf("初始化成功。\n");
                    init = initStack(&sqstack,size);
                }
                else
                    printf("初始化失败。\n");
                break;
            case 2:
                if(init == SUCCESS)
                    if(isEmptyStack(&sqstack))
                        printf("栈空。\n");
                    else printf("栈不为空。\n");
                else
                    printf("未进行初始化，请重新输入。\n");
                break;
            case 3:
                if(init == SUCCESS)
                {
                    ElemType e;
                    if(getTopStack(&sqstack,&e))
                        printf("栈顶元素：%d\n",e);
                    else
                        printf("获取栈顶元素失败。\n");
                }
                else
                    printf("未进行初始化，请重新输入。\n");
                break;
            case 4:
                if(init == SUCCESS){
                    if(clearStack(&sqstack))
                        printf("清空栈成功。\n");
                    else
                        printf("清空失败。\n");
                }
                else
                    printf("未进行初始化，请重新输入。\n");
                break;
            case 5:
                if(init == SUCCESS)
                    if(destroyStack(&sqstack))
                        printf("销毁栈成功。\n");
                    else
                        printf("销毁栈失败。\n");
                else
                    printf("未进行初始化，请重新输入。\n");
                break;
            case 6:
                if(init == SUCCESS)
                {
                    int length;
                    if(stackLength(&sqstack,&length))
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
                    if(pushStack(&sqstack,data))
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
                    ElemType data;
                    if(popStack(&sqstack,&data))
                        printf("出栈数据：%d\n",data);
                    else
                        printf("出栈失败。\n");
                }
                else
                    printf("未进行初始化，请重新输入。\n");
                break;
        }

        printf("输入操作数<1-8>（输入q退出）:");
        scanf("%d",&choice);

        while(getchar() != '\n')
            continue;
    }

    printf("Done.");

    return 0;
}
