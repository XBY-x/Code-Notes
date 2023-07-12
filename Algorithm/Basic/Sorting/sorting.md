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


### Merge sort (归并排序)
#### 步骤
![v2-a29c0dd0186d1f8cef3c5ebdedf3e5a3_b](https://user-images.githubusercontent.com/57653726/187385874-c22707b9-4d26-468e-b0b6-66bd6348fb15.gif)


```
# 归并排序中的思路
MergeSort(arr[], l,  r)
If r > l
     1. 找到数组中的中间点，把数组分为两部分
             middle m = (l+r)/2
     2. 对数组的左部分调用MergeSort 函数  
             Call mergeSort(arr, l, m)
     3. 对数组的右部分调用MergeSort 函数 
             Call mergeSort(arr, m+1, r)
     4. 合并2,3中的两部分
             Call merge(arr, l, m, r)
```

#### python3
```python
def merge_arr(a, b):
    res = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1
    while i < len(a):
        res.append(a[i])
        i += 1
    while j < len(b):
        res.append(b[j])
        j += 1
    return res

def merge_sort(arr):
    arr_len = len(arr)
    if arr_len <= 1:
        return arr
    mid = arr_len >> 1
    return merge_arr(merge_sort(arr[:mid]), merge_sort(arr[mid:]))
```

### Heap sort (堆排序)
#### tips:
- 堆：
  
  堆是 完全二叉树 结构
- 完全二叉树
  
  在一颗二叉树中，若除最后一层外的其余层都是满的，并且最后一层要么是满的，要么在右边缺少连续若干节点，
  
  则此二叉树为完全二叉树（Complete Binary Tree）
- 堆节点下标的计算
  
  对于 节点 i
    - 左子节点 2i + 1
    - 左子节点 2i + 2
    - 父节点  (i-1) / 2
- 大顶堆：每个结点的值都大于或等于其左右孩子结点的值

  小顶堆：每个结点的值都小于或等于其左右孩子结点的值

- 一般升序排序采用大顶堆
  
  降序排序采用小顶堆

#### 步骤
先将无需序列构造成一个堆结构，然后逐步构建 大顶堆/小顶堆
从最后一个父节点开始倒着排序，直到本趟排序完成
将堆顶的元素(是 最大/最小 元素) 与 序列最末尾元素交换
继续对 去掉有序的最后一个元素的序列进行排序，重复此过程，直到排序完成。

#### 例
(画二叉树看更清晰)

#### C 实现 (升序排序)
```c
void swap(int* a, int* b) {
    int temp = *b;
    *b = *a;
    *a = temp;
}

void max_heapify(int arr[], int start, int end) {
    int dad = start;
    int son = dad * 2 + 1;  // 左子节点
    while (son <= end) {
        if (son + 1 <= end && arr[son] < arr[son + 1]) // 找到两个子节点中较大的那个 
            son++;
        if (arr[dad] > arr[son]) //父 > 子，调整完毕，退出
            return;
        else { // 交换父子内容后，继续处理子节点和孙节点的关系
            swap(&arr[dad], &arr[son]);
            dad = son;
            son = dad * 2 + 1;
        }
    }
}

void heap_sort(int arr[], int len) {
    /* 计算最后一个父节点：
    *    已知数组长度(节点个数) 为 len,
    *    那么最后一个节点的下标就是 (len - 1),
    *    因为堆是完全二叉树结构，所以最后一个节点的父节点，就是这个二叉树中最后一个有子节点的节点(最后一个父节点)，
    *    带入 (i-1) / 2 计算 (len - 1)的父节点, 得到父节点下标为 (len - 2) / 2  也就是 len / 2 - 1
    */
    // 从最后的父节点开始调整
    for (int i = len / 2 - 1; i >= 0; i--) 
        max_heapify(arr, i, len - 1);

    // 经过上面的处理， 此时堆的根节点[第0个]是序列的最大值

    for (int i = len - 1; i > 0; i--) {
        // 交换 根节点([0]) 和 未排序序列的最后一个元素，交换后 原未排序序列的最后一个元素 为 原未排序序列的最大值
        swap(&arr[0], &arr[i]);
        // 继续排 原未排序序列-1 的序列， 此时 前半部分为新的未排序序列，是原始序列的最大n个值的有序序列
        max_heapify(arr, 0, i - 1);
    }
}
```

#### python3 实现 (升序排序)
```python
def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]


def max_heapify(arr, start, end):
    dad = start
    son = dad * 2 + 1  # 左子节点
    while son <= end:
        if son+1 <= end and arr[son] < arr[son+1]:
            son += 1  # 右子节点大于左子节点， 所以让son变成右子节点
        if arr[dad] >= arr[son]:  # 父节点 大于 子节点，说明本次调节完成，return
            return
        else:
            swap(arr, dad, son)
            dad = son  # 让子节点成为新的父节点，继续调节子树的节点
            son = dad * 2 + 1


def heap_sort(arr):
    arr_len = len(arr)
    # 先从 完全二叉树中 的 最后一个 父节点 开始，倒着将每个父节点都处理一遍
    # 最后一个父节点，也就是 树 的 最后一个节点的父节点, 也就是下标 len(arr)-1的节点的父节点
    # 所以最后一个父节点的下标为： ((len(arr)-1) - 1) // 2 也就是 (len(arr) // 2 - 1)
    for i in range(arr_len // 2 - 1, -1, -1):
        max_heapify(arr, i, arr_len-1)

    for i in range(arr_len - 1, 0, -1):
        swap(arr, 0, i)
        max_heapify(arr, 0, i - 1)


input_arr = [7, 2, 9, 7, 3, 1, 5, 6, 1, 0]
heap_sort(input_arr)
print(input_arr)
```






### Quick sort (快速排序)
#### 步骤
先选择数据中的某一个元素为中心点(pivot) (一般选第0个元素);

把 比pivot小的值 放到 pivot 左边， 把 比pivot大的值 放到 pivot 右边； (这一过程被称为分割/分区 (partition). 分区结束后，pivot现在所在的位置就是排序结束后的最终位置。)

分别对 pivot 的 左边 和 右边 两个未排序序列进行上面的操作， 直到 pivot 左 右 都只有1个元素。

```
input_arr is:
50 36 66 76 36 12 25 95

<初始>  [50] 36 66 76 36 12 25 95

<第1趟> 25 36 12 36 [50] 76 66 95    // 以 [50] 为中心点，对整体进行快排

       |----------------|     |-----------|
<第2趟> | 12 [25] 36 36 | [50] | 76 66 95 |  // 对 [50] 左边进行快排
       |----------------|     |-----------|

       |-----|-----|----------|     |-----------|
<第3趟> | 12 | [25] | [36] 36 | [50] | 76 66 95 |  // 分别对 [25]左右 进行快排
       |-----|-----|----------|     |-----------|

                        |-------------|
<第4趟> 12 25 36 36 [50] | 66 [76] 95 |  // 对 [50] 右边 进行快排
                        |-------------|
```



#### python3
```python
def quick_sort(arr, low, high):
    if low >= high:
        return
    pivot = paritition(arr, low, high)
    quick_sort(arr, low, pivot-1)
    quick_sort(arr, pivot+1, high)


def paritition(arr, low, high):
    pivot = arr[low]
    while low < high:
        while low < high and arr[high] > pivot:
            high -= 1
        arr[low] = arr[high]
        while low < high and arr[low] <= pivot:
            low += 1
        arr[high] = arr[low]
    arr[low] = pivot
    return low

a = [3,2,3,1,2,4,5,5,6]
quick_sort(a, 0, len(a)-1)
```

#### C
```c
int Paritition(int A[], int low, int high) {
    int pivot = A[low];
    while (low < high) {
        while (low < high && A[high] >= pivot) {
            high--;
        }
        A[low] = A[high];
        while (low < high && A[low] <= pivot) {
            low++;
        }
        A[high] = A[low];
    }
    A[low] = pivot;
    return low;
}

void QuickSort(int A[], int low, int high)
{
    if (low < high) {
        int pivot = Paritition(A, low, high);
        QuickSort(A, low, pivot - 1);
        QuickSort(A, pivot + 1, high);
    }
}
```

### Shellsort
#### 步骤
一般选 初始步长 gap = length >> 1  (也就是 数据长 对 2 取整)

![image](https://user-images.githubusercontent.com/57653726/187371994-afa4217d-2339-4477-b470-926e6de032ff.png)

#### python3
```python
def shell_sort(arr):
    arr_len = len(arr)
    gap = arr_len >> 1
    while gap > 0:
        for i in range(gap, arr_len):
            temp = arr[i]

            j = i - gap
            while j >= 0 and arr[j] > temp:
                arr[j + gap] = arr[j]
                j -= gap
            arr[j + gap] = temp
        gap >>= 1
```


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

