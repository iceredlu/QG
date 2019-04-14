# include <stdio.h>
# include <stdlib.h>
# include <string.h>
# include <time.h>
# include "sort.h"
# define NUM 11

void sort_menu()
{
    char menu [NUM][50] = {
    "***********************",
    "**       SORT        **",
    "***********************",
    "**      1.INS        **",
    "**      2.MER        **",
    "**      3.QUI        **",
    "**      4.COU        **",
    "**      5.RAD        **",
    "**      6.Color      **",
    "**      7.Search     **",
    "***********************",
    };

    for(int i=0; i < NUM; i++)
        printf("%s\n",menu[i]);
}

void sort_method(int method,int *a,int n)
{
    switch(method)
    {
        case 1:
            insertSort(a,n);
            printArray(a,n);
            break;
        case 2:
            {
            int temp[n];
            MergeSort(a,0,n,temp);
            printArray(a,n);
            break;
            }
        case 3:
            QuickSort_Recursion(a, 0, n);
            printArray(a,n);
            break;
        case 4:
            {
            int max;
            printf("enter max for array:");
            scanf("%d",&max);
            CountSort(a,n,max);
            printArray(a,n);
            break;
            }
        case 5:
            RadixCountSort(a,n);
            printArray(a,n);
            break;
        case 6:
            ColorSort(a,n);
            printArray(a,n);
            break;
        case 7:
            {
                SearchNum(a,n);
                break;
            }
    }
}

//打印数组
void printArray(int *a,int length)
{
    printf("sorted array:");
    for(int i=0; i< length; i++)
        printf("%d ",a[i]);
    printf("\n");
}

// 插入排序
void insertSort(int *a,int n)
{
    for(int i=1; i<n; i++)  //从第二个数开始遍历
    {
        int temp = a[i];
        int j;
        for(j=i-1; j>=0 && (a[j]>temp); j--)//与索引指向的值前面的数组逐个比较寻找插入位置
            a[j+1] = a[j];
        a[j+1] = temp;
    }
}

//归并排序（合并数组）
void MergeArray(int *a,int begin,int mid,int end,int *temp)
{
    int pb,pe,pt;//分别指向前半部分数组后半部分数组、承载数组
    pb=begin, pe=mid+1, pt= begin;
    //前半部分数组和后半部分数组都未遍历结束前，比较pb、pe所指向元素大小选取存入数值
    while(pb <= mid && pe <= end)
    {
        if(a[pb] <= a[pe])
            temp[pt++] = a[pb++];
        else
            temp[pt++] = a[pe++];
    }
    //将剩下的元素输入temp
    while(pb <= mid)
        temp[pt++] = a[pb++];
    while(pe <= end)
        temp[pt++] = a[pe++];
    //temp复制到a
    memcpy(a+begin,temp+begin,(end-begin+1)*sizeof(int));
}
//归并排序
void MergeSort(int *a,int begin,int end,int *temp)
{
    if(begin < end)
    {
        int mid = (begin+end)/2;
        //分割数组
        MergeSort(a,begin,mid,temp);
        MergeSort(a,mid+1,end,temp);
        //合并数组
        MergeArray(a,begin,mid,end,temp);
    }
}

//快速排序（枢轴存放）
int Partition(int *a, int begin, int end)
{
    int key = a[begin];

    while(begin!=end)
    {
        while(a[end] >= key && begin < end)
            end--;
        if(end > begin)
            a[begin] = a[end];
        while(a[begin] <= key && begin < end)
            begin++;
        if(begin<end)
            a[end] = a[begin];
    }
    a[begin] = key;

    return begin;
}


//递归版快排
void QuickSort_Recursion(int *a, int begin, int end)
{
    if(begin >= end)
        return;

    int key = Partition(a,begin,end);

    QuickSort_Recursion(a,begin,key-1);
    QuickSort_Recursion(a,key+1,end);
}


//计数排序
void CountSort(int *a, int size , int max)
{
    //计数数组，统计数组a中各元素出现的次数
    int countArray[max];
    //用于存放已有序列的数组
    int sortArray[size];

    //初始化计数数组
    for(int i=0; i<size; i++)
        countArray[i] = 0;

    //统计次数
    for(int i=0; i< size; i++)
        countArray[a[i]]++;

    //统计比i小的数的个数，循环结束countArray[i]表示数组a中小于等于a的元素的个数
    for(int i=1; i < max; i++)
        countArray[i] += countArray[i-1];

    //反向填充
    for(int i=size;i > 0; i--)
    {
        int elem = a[i-1];
        int index = countArray[elem]-1;
        sortArray[index] = elem;
        countArray[elem]--;
    }

    memcpy(a,sortArray,size*sizeof(int));
}


// 找到num的从低到高的第pos位的数据
int GetNumInPos(int num,int pos)
{
	int temp = 1;
	for (int i = 0; i < pos - 1; i++)
		temp *= 10;

	return (num / temp) % 10;
}


//基数计数排序
void RadixCountSort(int *a,int size)
{
    int *radixArrays[10];    //分别为0~9的序列空间
	for (int i = 0; i < 10; i++)
	{
		radixArrays[i] = (int *)malloc(sizeof(int) * (size + 1));
		radixArrays[i][0] = 0;    //index为0处记录这组数据的个数
	}

	for (int pos = 1; pos <= 5; pos++)    //从个位开始到5位
	{
		for (int i = 0; i < size; i++)    //分配过程
		{
			int num = GetNumInPos(a[i], pos);
			int index = ++radixArrays[num][0];
			radixArrays[num][index] = a[i];
		}

		for (int i = 0, j =0; i < 10; i++)    //收集
		{
			for (int k = 1; k <= radixArrays[i][0]; k++)
				a[j++] = radixArrays[i][k];
			radixArrays[i][0] = 0;    //复位
		}
	}

}

//颜色排序
void ColorSort(int *a,int size)
{
    int p0,p2;
    p0=0,p2=size-1;

    for(int i=1; i<size && i != p2; i++)
    {
        while(a[i] == 0 || a[i] == 2)
        {
            if(a[i] == 0)
                swap(&a[i],&a[p0++]);
            else
                swap(&a[i],&a[p2--]);
        }
    }

}

void swap(int *a,int *b)
{
    int t = *a;
    *a = *b;
    *b = t;
}

void SearchNum(int *a,int size)
{
    int k;
    printf("enter the number you want to search:");
    scanf("%d",&k);

    QuickSort_Recursion(a,0,size);

    printf("num %d:%d\n",k,a[k-1]);
}
