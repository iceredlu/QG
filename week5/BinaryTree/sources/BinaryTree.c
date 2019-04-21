# include <stdio.h>
# include <stdlib.h>
# include "BinaryTree.h"

int pos = 0;

void menu()
{
    char menu[12][50] = {
    "************************************",
    "**        Binary Tree             **",
    "************************************",
    "**   1.Initialize binary tree     **",
    "**   2.Destroy binary tree        **",
    "**   3.Creat binary tree          **",
    "**   4.Pre-order traverse         **",
    "**   5.In-order traversal         **",
    "**   6.Post-order traversal       **",
    "**   7.Level order traverse       **",
    "**   8.Calculate prefix expression**",
    "************************************"
    };

    printf("\n\n");

    for(int i=0; i<12; i++)
        printf("%s\n",menu[i]);

    printf("\n\n");
}

void operatFun(BiTree T)
{
    Status init = ERROR;//用于判断是否已初始化
    Status isCreat = ERROR;
    int Operand;
    printf("input operand(1-8,0 to quit):");
    while(1)
    {
        if(!scanf("%d",&Operand))
        {
            while(getchar()!='\n')
                continue;
            printf("not a number,you need to enter a number between 1 and 8.\ntry again:");
            continue;
        }
        else if(Operand < 1 || Operand >8)
        {
            if(Operand == 0)
            {
                printf("byb~\n");
                break;
            }
            printf("wrong range,you need to enter a number between 1 and 8.\ntry again:");
            continue;
        }


        switch(Operand)
        {
            case 1:
                init = InitBiTree(&T);
                if(init)
                    printf("initialization successful.\n");
                break;
            case 2:
                if(init)
                {
                    if(DestroyBiTree(&T));
                        printf("destroy the binary tree successfully.\n");
                }
                else
                    printf("please initialize first.\n");
                break;
            case 3:
            {
                if(init)
                {
                    printf("input expression to creat binary tree(Use '#' to indicate an empty subtree):\n");
                    char a[100];
                    scanf("%s",a);
                    int count=0,length = 0;//计算输入的'#'数目，判断是否输入正确
                    for(int i=0; a[i]!='\0';i++)
                    {
                        if(a[i] == '#')
                            count++;
                        length++;
                    }
                    if(length/2+1 == count)//输入正确
                        isCreat = CreateBiTree(&T,a);
                    else
                    {
                        printf("wrong enter,try again.\n");
                        break;
                    }
                    if(isCreat)
                        printf("constructing a binary tree successfully.\n");
                }
                else
                    printf("please initialize first.\n");
                break;
            }
            case 4:
                if(isCreat)
                {
                    if(PreOrderTraverse(T,visit))
                        printf("\ntraversal completed.\n");
                }
                else
                    printf("please creat a binary tree first.\n");
                break;
            case 5:
                if(isCreat)
                {
                    if(InOrderTraverse(T,visit))
                        printf("\ntraversal completed.\n");
                }
                else
                    printf("please creat a binary tree first.\n");
                break;
            case 6:
                if(isCreat)
                {
                    if(PostOrderTraverse(T,visit))
                        printf("\ntraversal completed.\n");
                }
                else
                    printf("please creat a binary tree first.\n");
                break;
            case 7:
                if(isCreat)
                {
                    if(LevelOrderTraverse(T,visit))
                        printf("\ntraversal completed.\n");
                }
                else
                    printf("please creat a binary tree first.\n");
                break;
            case 8:
                {
                    int result = Value(T);
                    if(result > 1000 || result < -1000)
                    {
                        printf("wrong enter,try again.\n");
                        break;
                    }
                    printf("=%d\n",result);
                    break;
                }
        }
        printf("input operand(1-8,0 to quit):");
    }
}


//二叉树初始化
Status InitBiTree(BiTree *T)
{
    *T = NULL;
    pos = 0;
    return SUCCESS;
}


//构建二叉树
Status CreateBiTree(BiTree *T, char* definition)
{
    char c = definition[pos++];

    (*T) = (BiTree)malloc(sizeof(BiTNode));
    (*T)->data = c;
    (*T)->lchild = NULL;
    (*T)->rchild = NULL;

    if(c!='#')
    {
        CreateBiTree(&((*T)->lchild),definition);
        CreateBiTree(&((*T)->rchild),definition);
    }


    return SUCCESS;

}


//销毁二叉树
Status DestroyBiTree(BiTree *T)
{
    if(*T != NULL)
    {
        DestroyBiTree(&((*T)->lchild));
        DestroyBiTree(&((*T)->rchild));
        free(*T);
    }
    return SUCCESS;
}

//遍历函数
Status visit(TElemType e)
{
    if(e != '#')
        printf("%c",e);
    return SUCCESS;
}

//先序遍历
Status PreOrderTraverse(BiTree T, Status (*visit)(TElemType e))
{
    if(T)
    {
        visit(T->data);
        PreOrderTraverse(T->lchild,visit);
        PreOrderTraverse(T->rchild,visit);
    }
    return SUCCESS;
}

//中序遍历
Status InOrderTraverse(BiTree T, Status (*visit)(TElemType e))
{
    if(T)
    {
        InOrderTraverse(T->lchild,visit);
        visit(T->data);
        InOrderTraverse(T->rchild,visit);
    }
    return SUCCESS;
}

//后序遍历
Status PostOrderTraverse(BiTree T, Status (*visit)(TElemType e))
{
    if(T)
    {
        PostOrderTraverse(T->lchild,visit);
        PostOrderTraverse(T->rchild,visit);
        visit(T->data);
    }
    return SUCCESS;
}

//层序遍历
Status LevelOrderTraverse(BiTree T, Status (*visit)(TElemType e))
{
    Queue Q;
    initQueue(&Q);
    if(T)
    {
        EnQueue(&Q,T->data);
        visit(T->data);
    }
    while(Q.length != 0)
    {
        DeQueue(&Q);
        if(T->lchild)
        {
            visit(T->lchild->data);
            EnQueue(&Q,T->lchild->data);
        }
        if(T->rchild)
        {
            visit(T->rchild->data);
            EnQueue(&Q,T->rchild->data);
        }
        if(T->lchild)
            T = T->lchild;
        else if(T->rchild)
            T = T->rchild;
    }
    return SUCCESS;
}

//初始化队列
void initQueue(Queue * Q)
{
    Q->front = Q->rear = (QueNode*)malloc(sizeof(QueNode));
    Q->length = 0;
}

//入队操作
void EnQueue(Queue *Q,TElemType e)
{
    Q->rear->next = (QueNode*)malloc(sizeof(QueNode));
    Q->rear = Q->rear->next;
    Q->rear->data = e;
    Q->length ++;
}

//出队操作
void DeQueue(Queue *Q)
{
    QueNode *p = Q->front;
    Q->front = Q->front->next;
    free(p);
    (Q->length) --;
}

//输入前缀表达式并计算结果
int Value(BiTree T)
{
    InitBiTree(&T);
    printf("input prefix expression(Use '#' to indicate an empty subtree):\n");
    char a[100];
    scanf("%s",a);
    //创建二叉树
    int result;//计算结果
    int count=0,length = 0;//计算输入的'#'数目，判断是否输入正确
    for(int i=0; a[i]!='\0';i++)
    {
        if(a[i] == '#')
            count++;
        length++;
    }
    if(length/2+1 == count)//输入正确
    {
        CreateBiTree(&T,a);
        if(isOper(T->data))
            result = cal(T);
        //以中缀输出表达式
        InOrderTraverse(T,visit);
    }
    return result;
}


//计算,类似中序遍历
int cal(BiTree T)
{
    int result;
    char c = T->data;
    if(isOper(T->data))//若为操作符，分别计算左右子树
    {
        switch(c)
        {
            case '+':
                result =  cal(T->lchild) + cal(T->rchild);
                break;
            case '*':
                result = cal(T->lchild) * cal(T->rchild);
                break;
            case '-':
                result = cal(T->lchild) - cal(T->rchild);
                break;
            case '/':
                result = cal(T->lchild) / cal(T->rchild);
                break;
        }
    }
    if(isNum(T->data)) //数字为叶子节点，直接返回
    {
        result = T->data - '0';
    }
    return result;
}

//判断是否数字
Status isNum(TElemType e)
{
    if(e >= '1' && e <= '9')
        return SUCCESS;
    return ERROR;
}

//判断是否操作符
Status isOper(TElemType e)
{
    char oper[4] = {'+','-','*','/'};

    for(int i=0; i<4; i++)
    {
        if(e == oper[i])
            return SUCCESS;
    }
    return ERROR;
}



