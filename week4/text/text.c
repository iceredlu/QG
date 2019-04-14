# include <stdio.h>
# include <stdlib.h>
# include <string.h>
# include <time.h>
# include "text.h"

//生成随机数组
void initArray(int *a,int count)
{
    srand(time(NULL));
    int index=0;
    while(index != count)
    {
        int t = rand() % 32768;
        a[index++] = t;
    }
}

//保存到文件
void saveArray(int *a,int count)
{
    FILE *fp = fopen("D:\\data\\text_rand.txt","wt");

    if(fp)
    {
        for(int i=0; i<count; i++)
            fprintf(fp,"%d\n",a[i]);
    }
    fclose(fp);
}

//读取文件
void readArray(int *a,int count)
{

    FILE *fp = fopen("D:\\data\\text_rand.txt","r");

    if(fp)
    {
        for(int i=0; i<count; i++)
            fscanf(fp,"%d",&a[i]);
    }
    fclose(fp);
}

void text_amount(int *a,int count)
{
    double duration[5];

    char method [5][20] = {"insert sort","merge sort","quick sort","count sort","radixcount sort"};

    clock_t start,finish;

    start = clock();
    insertSort(a,count);
    finish = clock();
    duration[0] = (double)(finish- start);
    printf("%s:%lf\n",method[0],duration[0]);

    start = clock();
    int temp[count];
    MergeSort(a,0,count-1,temp);
    finish = clock();
    duration[1] = (double)(finish- start);
    printf("%s:%lf\n",method[1],duration[1]);

    start = clock();
    QuickSort_Recursion(a,0,count-1);
    finish = clock();
    duration[2] = (double)(finish- start);
    printf("%s:%lf\n",method[2],duration[2]);

    start = clock();
    RadixCountSort(a,count);
    finish = clock();
    duration[4] = (double)(finish- start);
    printf("%s:%lf\n",method[4],duration[4]);

    start = clock();
    int max = a[0];
    for(int i=1; i<count; i++)
        if(a[i] > max)
            max = a[i];
    CountSort(a,count,max);
    finish = clock();
    duration[3] = (double)(finish- start);
    printf("%s:%lf\n\n\n",method[3],duration[3]);

}

void text_array(int *a,int count,int num)
{
    double duration[5];

    char method [5][20] = {"insert sort","merge sort","quick sort","count sort","radixcount sort"};

    clock_t start,finish;

    start = clock();
    for(int i=0; i<num; i++)
    {
        initArray(a,count);
        insertSort(a,count);
    }
    finish = clock();
    duration[0] = (double)(finish- start);
    printf("%s:%lf\n",method[0],duration[0]);

    start = clock();
    for(int i=0; i<num; i++)
    {
        initArray(a,count);
        int temp[count];
        MergeSort(a,0,count-1,temp);
    }
    finish = clock();
    duration[1] = (double)(finish- start);
    printf("%s:%lf\n",method[1],duration[1]);

    start = clock();
    for(int i=0; i<num; i++)
    {
        initArray(a,count);
        QuickSort_Recursion(a,0,count-1);
    }
    finish = clock();
    duration[2] = (double)(finish- start);
    printf("%s:%lf\n",method[2],duration[2]);

    start = clock();
    for(int i=0; i<num; i++)
    {
        initArray(a,count);
        RadixCountSort(a,count);
    }
    finish = clock();
    duration[4] = (double)(finish- start);
    printf("%s:%lf\n",method[4],duration[4]);

    start = clock();
    for(int i=0; i<num; i++)
    {
        initArray(a,count);
        int max = a[0];
        for(int i=1; i<count; i++)
            if(a[i] > max)
                max = a[i];
    CountSort(a,count,max);
    }
    finish = clock();
    duration[4] = (double)(finish- start);
    printf("%s:%lf\n",method[4],duration[4]);
}

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


void swap(int *a,int *b)
{
    int t = *a;
    *a = *b;
    *b = t;
}
