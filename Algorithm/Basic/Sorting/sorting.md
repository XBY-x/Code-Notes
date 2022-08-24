# Sorting algorithm

### Insertion sort (插入排序)
#### 步骤
将第一待排序序列第一个元素看做一个有序序列，把第二个元素到最后一个元素当成是未排序序列。
从头到尾依次扫描未排序序列，将扫描到的每个元素插入有序序列的适当位置。（如果待插入的元素与有序序列中的某个元素相等，则将待插入元素插入到相等元素的后面。）

#### 例：
```
input_arr is:
2 7 4 5 1 2 6 7 10 3
[0] is: 2 7 4 5 1 2 6 7 10 3
[1] is: 2 7 4 5 1 2 6 7 10 3
[2] is: 2 4 7 5 1 2 6 7 10 3
[3] is: 2 4 5 7 1 2 6 7 10 3
[4] is: 1 2 4 5 7 2 6 7 10 3
[5] is: 1 2 2 4 5 7 6 7 10 3
[6] is: 1 2 2 4 5 6 7 7 10 3
[7] is: 1 2 2 4 5 6 7 7 10 3
[8] is: 1 2 2 4 5 6 7 7 10 3
[9] is: 1 2 2 3 4 5 6 7 7 10
```

#### C 语言实现
```c
void insertion_sort(int arr[], int len) {
    int current = 0;
    int index = 0;
    for (int i = 0; i < len; i++)
    {
        current = arr[i];
        index = i;
        while ((index > 0) && (current < arr[index - 1]))
        {
            arr[index] = arr[index - 1];
            index -= 1;
        }
        arr[index] = current;
    }
}
```
### Binary insertion sort (折半插入排序)
基本概念
折半插入排序（binary insertion sort）是对插入排序算法的一种改进，由于排序算法过程中，就是不断的依次将元素插入前面已排好序的序列中。由于前半部分为已排好序的数列，这样我们不 用按顺序依次寻找插入点，可以采用折半查找的方法来加快寻找插入点的速度。
https://developer.aliyun.com/article/31759


### Selection sort (选择排序)
#### 步骤
首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置。
再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
重复第二步，直到所有元素均排序完毕。

#### 例
```
input_arr is:
2 7 4 5 1 2 6 7 10 3
[0] 1 7 4 5 2 2 6 7 10 3
[1] 1 2 4 5 7 2 6 7 10 3
[2] 1 2 2 5 7 4 6 7 10 3
[3] 1 2 2 3 7 4 6 7 10 5
[4] 1 2 2 3 4 7 6 7 10 5
[5] 1 2 2 3 4 5 6 7 10 7
[6] 1 2 2 3 4 5 6 7 10 7
[7] 1 2 2 3 4 5 6 7 10 7
[8] 1 2 2 3 4 5 6 7 7 10
```

#### C语言实现
```c
void selection_sort(int arr[], int len)
{
    int temp = 0;
    int min_index = 0;

    // 这里 i < len-1 是因为内部循环是 j=i+1 开始的。
    // 最后循环到 i等于倒数第2个元素 的时候，已经让 -1 和 -2 元素做了比较，已经交换过，是有序的；
    // 所以不需要再让 i 等于最后一个元素下标了
    for (int i = 0; i < len - 1; i++)
    {
        min_index = i;
        for (int j = i + 1; j < len; j++)
        {
            if (arr[j] < arr[min_index])
            {
                min_index = j;
            }
        }
        if (min_index != i)
        {
            temp = arr[i];
            arr[i] = arr[min_index];
            arr[min_index] = temp;
        }
    }
}
```

#### python3
``` python
def selection_sort(arr):
    for i in range(len(arr)-1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
```


### Merge sort
### Heapsort

### Quicksort (快速排序)
#### 步骤

### Shellsort


### Bubble sort (冒泡排序)
#### 步骤
比较相邻的元素。如果第一个比第二个大，就交换他们两个。
对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，**最后的元素会是最大的数**。

针对所有的元素重复以上的步骤，**除了最后一个**。
持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。

也就是做了n次遍历后，末尾的n个数就是从小到大的最大n个数。

#### 例
```
input_arr is:
2 7 4 5 1 2 6 7 10 3
[0] 2 4 5 1 2 6 7 7 3 10
[1] 2 4 1 2 5 6 7 3 7 10
[2] 2 1 2 4 5 6 3 7 7 10
[3] 1 2 2 4 5 3 6 7 7 10
[4] 1 2 2 4 3 5 6 7 7 10
[5] 1 2 2 3 4 5 6 7 7 10
[6] 1 2 2 3 4 5 6 7 7 10
[7] 1 2 2 3 4 5 6 7 7 10
[8] 1 2 2 3 4 5 6 7 7 10
[9] 1 2 2 3 4 5 6 7 7 10
```
#### C语言实现
```c
void bubble_sort(int arr[], int len)
{
    int temp = 0;
    int i = 0;
    for (int i = len; i > 0; i--)
    {
        for (int j = 1; j < i; j++)
        {
            if (arr[j - 1] > arr[j])
            {
                temp = arr[j];
                arr[j] = arr[j - 1];
                arr[j - 1] = temp;
            }
        }
    }
}
```

### Counting sort
### Bucket sort
### Radix sort

