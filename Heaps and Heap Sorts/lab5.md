# Lab 5 Reflection and Observations

* Anuj Verma
* Avni Goyal
* name of team member 3

## Heap Insertion

### Picture of heap created with 10 values
![WhatsApp Image 2023-07-14 at 8 26 16 AM](https://github.com/seneca-dsa456/averma100/assets/113152048/2fdfb5ff-c511-47a0-ad50-80d8dfc5e5b5)


### Pictures of adding 11th value to heap
![2](https://github.com/seneca-dsa456/averma100/assets/113152048/ccc96d6b-158c-45ef-87ee-985c0ac9797a)


## Heap Removal

### Picture after 1 value was removed from heap
![rem](https://github.com/seneca-dsa456/averma100/assets/113152048/dee9c985-99a5-488f-8ab5-5a92c5225fcf)


### Values removed (in order removed):
3

## Array representation of heap

### Picture of heap and Array representation of heap
![imgstep2](https://github.com/seneca-dsa456/averma100/assets/113152048/dc8bbbd4-d53e-4816-aa00-c425e865b499)


## Creating a heap from array

### Photograph of your array and heap
![part d](https://github.com/seneca-dsa456/averma100/assets/113152048/4e6828be-d51c-45f7-834c-2dd62a76d4a3)


* What number is the first non-leaf node starting from bottom?
* Answer - 35
* What index is that node at?
* Answer - 4


### Photograph of heap created by Heapify
![heaptree](https://github.com/seneca-dsa456/averma100/assets/113152048/006c2740-b939-45be-a957-dcdb3c0f7b32)


## HeapSort

Initial questions (do first):
how many values are in your array?
--> 11
what is index of last value in array?
--> 10

After doing 1 removal operation

* what was the first value removed? How does this number compare with others in heap (biggest? smallest?)
* --> 40, biggest
* Look at your heap portion of the array after you did this removal.. how many values are in it, what is the index of the bottom right most value in heap?
* --> 10, 9

After doing 2 removal operations:

* Perform another remove from the heap and adjust the array to match
* What was the second value removed and how does it compare with others still in heap?
* --> 38, biggest
* Look at your heap portion of the array after you did this removal.. how many values are in what is the index of the bottom right most value in heap?
* --> 9, 8
* Are there any open spots in the array that is not part of the heap and not holding anything useful?
* --> Yes, at index 9.

After doing 3 removal operations:

* Perform another remove from the heap and adjust the array to match
* What was the second value removed and how does it compare with others still in heap?
* --> 35, maximum
* Look at your heap portion of the array after you did this removal.. how many values are in it, what is the index of the bottom right most value in heap?
* --> 8, 7
* Are there any open spots in the array that is not part of the heap and not holding anything useful?
* Yes, at index 8.


## Reflection

This last part is to be completed individually.

Write a short paragraph about what you learned from this lab.
* Discuss what you learned about heaps and heap sort.
* --> Heaps is an intersting concept. A heap is a complete binary tree data structure that satisfies the heap property. In a max heap, for any given node, the value of the node is greater than or equal to the values of its children. In a min heap, the value of the node is smaller than or equal to the values of its children. Heaps are commonly implemented using arrays or dynamic memory allocation.
Heap Sort - Heap Sort is a sorting algorithm that utilizes the heap data structure to sort elements in ascending or descending order.
It consists of two main steps: building a heap from the input array (using heapify) and repeatedly extracting the maximum or minimum element from the heap and placing it in the sorted array.
* What was the most surprising thing you learned about heaps?
* --> Most surpirising fact about heap is that it can be expressed as arrays. A complex tree like structure can be stored as an array and its childs and parents can be accessed with a simple formula like 2i+1 and 2i+2. Also, its sorting time complexity is nlogn for
* all cases (best, worst and average)

