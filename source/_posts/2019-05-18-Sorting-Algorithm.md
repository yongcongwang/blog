---
title: Sorting Algorithm
date: 2019-05-18 16:20:11
categories: algorithm
mathjax: true
tags:
 - algorithm
 - data structure
---

## Assumption
To simplify matters, we will assume that the algorithms we describe will all be interchangeable:
1. All array positions contain data to be sorted;
2. The `N` is the number of elements passed to our sorting routines;
3. the `>` and `<` operators exists, which can be used to place a consistant ordering on the input.
Sorting under these conditions is known as comparision-based sorting.
<!-- more -->
## Visualization
To show the sorting process more in detail, we can draw each step of the algorithm with a bar graph and then combine them to a `gif`. Firstly, I plot the figure while two elements comparing, the code is below(take bubblesort as an example):
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# By yongcong.wang @ 30/09/2019
import matplotlib.pyplot as plt
import os


class fig_plot:
    def __init__(self):
        self.fig_cnt = 0
        self.figs = []

    def plot(self, arr, red_list):
        x = range(len(arr))
        bar_list = plt.bar(x, arr, color='k', width=0.95)
        plt.axis("off")
        plt.title(str(self.fig_cnt))
        for i, v in enumerate(arr):
            plt.text(x[i] - 0.45, v + 0.5, str(v))
        for index in red_list:
            bar_list[index].set_color("r")
        self.figs.append(plt.figure())
        plt.clf()
        self.fig_cnt += 1

    def show(self, index):
        self.figs[index].show()

    def save_pngs_to_folder(self, folder):
        path = "./" + folder
        if not os.path.exists(path):
            os.makedirs(path)
        cnt = 0
        for fig in self.figs:
            fig.savefig(path + "/" + str(cnt) + ".png")
            cnt += 1


def bubblesort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                tmp = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = tmp
            plot.plot(arr, [j, j+1])
    plot.save_pngs_to_folder("bubble")


plot = fig_plot()


def main():
    arr = [11, 9.2, 8.8, 23.6, 3.9, 14.1, 21.5, 33.3, 6.3, 13.6, 1.5]
    bubblesort(arr)


if __name__ == "__main__":
    main()
```

And then, I upload all the images and convert them to a gif at [Animated GIF Maker](https://ezgif.com/maker).

## Bubblesort
Bubblesort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order. The algorithm is a comparison sort, is named for the way smaller or larger elements "bubble" to the top of the list. Although the algorithm is simple, it is too slow and impractical for most problems even when compared to Insertionsort. Bubblesort can be practical if the input is in mostly sorted order with some out-of-order elements nearly in position.

```C++
template <typename T>
void swap(T &a, T &b) {
  T tmp = a;
  a = b; 
  b = tmp;
}

template <typename T>
void bubbleSort(std::vector<T> arr) {
  for (std::size_t i = 0, size = arr.size(); i < size - 1; ++i) {
    for (std::size_t j = 0; j < size - 1 - i; ++j) {
      if (arr[j] > arr[j + 1]) {
        swap(arr[j], arr[j + 1]);
      }
    }
  } 
}
```
![bubble sort](/images/2019-05-18-Sorting-Algorithm/bubble.gif)

## Insertionsort
One of the simplest sorting algorithms is the insertion sort.
Insertion sort consists of N - 1 passes. For pass p = 1 through N - 1, insertion sort ensures that the elements in position 0 through p are in sorted order. Insertion sort makes use of the fact that elements in position 0 through p - 1 are already known to be in sorted order.
```C++
template <typename T>
void insertSort(std::vector<T> &arr) {
  for (std::size_t i = 0, j, size = arr.size(); i < size; ++i) {
    T tmp = arr[i];
    for (j = i; j > 0 && tmp < arr[j - 1]; --j) {
      arr[j] = arr[j - 1];
    }
    arr[j] = tmp;
  }
}
```
Becuase of the nested loops, each of which can take N iterations, insertion sort is $O(N^2)$. Furthermore, this bound is tight, because input in reverse order can achieve this bound.
![insertion sort](/images/2019-05-18-Sorting-Algorithm/insertion.gif)

## Shellsort
Shellsort, named after its inventor, Donald Shell, was one of the first algorithms to break the quadratic time barrier, althoungh it was not until several years after its initial discovery that a subquadratic time bound was proven.
It works by comparing elements that are distant; the distance between comparisons decreases as the algorithm runs until the last phase, in which adjacent elements are compared. For this reason, Shellsort is sometimes referred to as diminishing increment sort.
Shellsort uses a sequence, h1, h2,…, ht, called increment sequence. Any increment sequence will do as long as h1 = 1, but some choices are better than others.
A popular(but poor) choice for increment sequence is to use the sequence suggested by Shell: $h_t = [N / 2]$ and $h_k = [h_{k + 1} / 2]$.
```C++
template <typename T>
void shellSort(std::vector<T> &arr) {
  for (std::size_t gap = arr.size() / 2; gap > 0; gap /= 2) {
    for (std::size_t i = gap, cnt = arr.size(); i < cnt; ++i) {
      auto tmp = arr[i];
      auto j = i;
      for (; j >= gap && tmp < arr[j - gap]; j -= gap) {
        arr[j] = arr[j - gap];
      }
      arr[j] = tmp;
    }
  }
}
```

The performance of Shellsort is quite acceptable in practice, even for N in the tens of thousands. The simplicity of the code makes it the algorithm of choice for sorting up to moderately large input.

## Heapsort
Priority queues can be used to sort in $O(NlogN)$ time. The algorithm based on this idea is known as heapsort and gives the best Big-Oh running time we have seen so far. The basic strategy is to build a binary heap of N elements. This stage takes $O(N)$ time. We then preform N deleteMin operations. The elements leave the heap smallest first, in sorted order. By recording these elements in a second array and then copying the array back, we sort N elements. Since each deleteMin takes $O(logN)$ time, the total running time is $O(NlogN)$.
The main problem with this algorithm is that it uses an extra array. Thus, the memory requirement is doubled. This could be a problem in some instances. Notice that the extra time spent copying the second array back to the first is only $O(N)$, so that this is not likely to affect the running time significantly. The problem is space.
A clever way to avoid using a second array makes use of the fact that after each deleteMin, the heap shrinks by 1. Thus the cell that was last in the heap can be used to store the element that was just deleted.
Using this strategy, after the last deleteMin the array will contain the elements in decreasing sorted order. If we want the elements in the more typical increasing sorted order, we can change the ordering property so that the parent has a larger elements than the child. Thus, we have a max-heap.

```C++
template <typename T>
void swap(T &a, T &b) {
  T tmp = a;
  a = b;
  b = tmp;
}

inline int getLeftChild(int hole) {
  return hole * 2 + 1;
}

template <typename T>
void percolateDown(std::vector<T> &arr, int hole, int heap_size) {
  T tmp = arr[hole];
  for (int child = getLeftChild(hole); child < heap_size; child = getLeftChild(hole)) {
    if (child != heap_size - 1 && arr[child + 1] > arr[child]) {
      ++child;
    }
    if (tmp < arr[child]) {
      arr[hole] = arr[child];
    } else {
      break;
    }
    hole = child;
  }
  arr[hole] = tmp;
}

template <typename T>
void heapSort(std::vector<T> &arr) {
  // build heap
  for (int cnt = arr.size(), i = cnt / 2; i >= 0; --i) {
    percolateDown(arr, i, cnt);
  }
  printArray(arr);
  // delete max
  for (int i = arr.size() - 1; i >= 0; --i) {
    swap(arr[0], arr[i]);
    percolateDown(arr, 0, i);
  }
}
```

## Mergesort
Mergesort runs in $O(NlogN)$ worse-case running time, and the number of comparisons used is nearly optimal. It is a fine example of a recursive algorithm.
The fundamental operation in this algorithm is merging two sorted lists. Because the lists are sorted, this can be done in one pass through the input, if the output is put in a third list. The basic merging algorithm takes two input array A and B, an output array C, and three counters, Actr, Bctr, and Cctr, which are initially set to the beginning of their respective arrays. The smaller of A[Actr] and B[Bctr] is copied to the next entry in C, and the appropriate counters are advanced. When either input list is exhausted, the remainder of the other list is copied to C.
```C++
template <typename T>
void merge(std::vector<T> &arr, std::vector<T> &temp_arr, int left_pos, int right_pos,
           int right_end) {
  int temp_pos = left_pos;
  int left_end = right_pos - 1;
  int ele_cnt = right_end - left_pos + 1;
  while (left_pos <= left_end && right_pos <= right_end) {
    if (arr[left_pos] < arr[right_pos]) {
      temp_arr[temp_pos++] = arr[left_pos++];
    } else {
      temp_arr[temp_pos++] = arr[right_pos++];
    }
  }

  while (left_pos <= left_end) {
    temp_arr[temp_pos++] = arr[left_pos++];
  }
  while (right_pos <= right_end) {
    temp_arr[temp_pos++] = arr[right_pos++];
  }

  for (int i = 0; i < ele_cnt; ++i, --right_end) {
    arr[right_end] = temp_arr[right_end];
  }
}

template <typename T>
void mergeSort(std::vector<T> &arr, std::vector<T> &temp_arr, int left, int right) {
  if (left < right) {
    int center = (right + left) / 2;
    std::cout << "left center right is " << left << ", " << center << ", " << right << std::endl;
    mergeSort(arr, temp_arr, left, center);
    mergeSort(arr, temp_arr, center + 1, right);
    merge(arr, temp_arr, left, center + 1, right);
  }
}

template <typename T>
void mergeSort(std::vector<T> &arr) {
  std::vector<T> temp_arr(arr.size());
  mergeSort(arr, temp_arr, 0, arr.size() - 1);
}
```
Mergesort is a classic example of the techniques used to analyze recursive routines: We have to write a recurrence relation for the running time. We will assume that N is a power of 2 so that we always split into even halves. For N = 1, the time to mergesort is constant, which we will denote by 1. Otherwise, the time to mergesort N numbers is equal to the time to do two recursive mergesort of size N/2, plus the time to merge, which is linear:
$$T(1) = 1$$
$$T(N) = 2T(N/2) + N$$

Although mergesort’s running time is $O(NlogN)$, it has the significant problem that merging two sorted lists uses linear extra memory. The additional work involved in copying to the temporary array and back, throughtout the algorithm, slows the sort considerably. This copying can be avoided by judiciously switching the roles of a and tmpArray at alternate levels of the recursion.
The running time of mergesort, when compared with other $O(NlogN)$ alternatives, depends heavily on the relative costs of comparing elements and moving elements in the array(and the temporary array). These costs are language dependent.

## Quicksort
As its name implies for C++, quicksort has historically been the fastest known generic sorting algorithm in practice. Its average running time is $O(NlogN)$. It is very fast, mainly due to a very tight and highly optimized inner loop. It has $O(N^2)$ worst-case performance, but this can be made exponentially unlikely with a little effort. By combining quicksort with heapsort, we can achieve quicksort’s fast running time on almost all inputs, with heapsort’s $O(NlogN)$ worst-case running time.
The quicksort algorithm is simple to understand and prove correct, although for many years it had the reputation of being an algorithm that could in theory be highly optimized but in practice was impossible to code correctly. Like mergesort, quicksort is a divide-and-conquer recursive algorithm.
The classic quicksort algorithm to sort an array S consists of the following four easy steps:
1. If the number of elements in S is 0 or 1, then return;
2. Pick any element v in S. This called the pivot;
3. Partition S-{v}(the remaining elements in S) into two disjoint groups: $S_1 = {x \in S - {v} | x \le v}$, and $S_x = {x \in S - {v} | x \ge v}$;
4. Return {quicksort($S_1$) followed by v followed by quicksort($S_2$)}.

For very small arrays($N \le 20$), quicksort does not perform as well as insertion sort. Furthermore, because quicksort is recursive, these cases will occur frequently. A comman solution is not to sue quicksort recursively for small arrays, but instead use a sorting algorithm that is efficient for small arrays, such as insertion sort. Using this strategy can actually save about 15 percent in the running time(over doing no cutoff at all). A good cutoff range is $N = 10$, although any cutoff between 5 and 20 is likely to produce similar results. This also saves nastly degenerate cases, such as taking the median of three elements when there are only one or two.
```C++
template <typename T>
T sortThreeElements(std::vector<T> &arr, int left, int right) {
  int mid = (left + right) / 2;
  if (arr[mid] < arr[left]) {
    swap(arr[mid], arr[left]);
  }
  if (arr[right] < arr[left]) {
    swap(arr[right], arr[left]);
  }
  if (arr[mid] > arr[right]) {
    swap(arr[mid], arr[right]);
  }

  swap(arr[mid], arr[right - 1]);
  return arr[right - 1];
}

template <typename T>
void insertSort(std::vector<T> &arr, int left, int right) {
  for (int i = left; i <= right; ++i) {
    T tmp = arr[i];
    int j;
    for (j = i; j > 0 && tmp < arr[j - 1]; --j) {
      arr[j] = arr[j - 1];
    }
    arr[j] = tmp;
  }
}

template <typename T>
void quickSort(std::vector<T> &arr, int left, int right) {
  if (right - left > 10) {
    int ptr_left = left;
    int ptr_right = right - 1;
    T pivot = sortThreeElements(arr, left, right);
    while (true) {
      while (arr[++ptr_left] < pivot);
      while (arr[--ptr_right] > pivot);
      if (ptr_left < ptr_right) {
        swap(arr[ptr_left], arr[ptr_right]);
      } else {
        break;
      }
    }
    swap(arr[ptr_left], arr[right - 1]);
    quickSort(arr, left, ptr_left - 1);
    quickSort(arr, ptr_right - 1, right);
  } else {
    insertSort(arr, left, right);
  }
}

template <typename T>
void quickSort(std::vector<T> &arr) {
  quickSort(arr, 0, arr.size() - 1);
}
```

















