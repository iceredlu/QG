#ifndef TEXT_H_INCLUDED
#define TEXT_H_INCLUDED

void initArray(int*,int);//生成数组

void saveArray(int*,int);//保存到文件

void text_amount(int*,int);//测试

void text_array(int *a,int count,int num);//大量小数组下的排序用时

void SearchNum(int *a,int size);

void sort_menu();//打印菜单

void sort_method(int method,int *a,int n);//选择排序方式

void printArray(int *a,int length);//打印数组

void swap(int *a,int *b);//交换元素

void RadixCountSort(int *a,int size);//基数计数排序

void CountSort(int *a, int size , int max);//计数排序

int Partition(int *a, int begin, int end);

void QuickSort_Recursion(int *a, int begin, int end);//快排

void MergeSort(int *a,int begin,int end,int *temp);//归并排序

void MergeArray(int *a,int begin,int mid,int end,int *temp);

void insertSort(int *a,int n);//插入排序

#endif
