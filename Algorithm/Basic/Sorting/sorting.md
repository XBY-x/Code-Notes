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
## Binary insertion sort (折半插入排序)
基本概念
折半插入排序（binary insertion sort）是对插入排序算法的一种改进，由于排序算法过程中，就是不断的依次将元素插入前面已排好序的序列中。由于前半部分为已排好序的数列，这样我们不 用按顺序依次寻找插入点，可以采用折半查找的方法来加快寻找插入点的速度。
https://developer.aliyun.com/article/31759


### Selection sort

### Merge sort
### Heapsort
### Quicksort
### Shellsort

### Bubble sort

### Counting sort
### Bucket sort
### Radix sort

