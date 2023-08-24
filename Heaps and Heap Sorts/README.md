
## Objectives:

- Learn all about heaps and heap sort


### Part A: Heap insertion

* As a group review the heap insertion algorithm
* Taking turns, insert each of the values into the heap to form a min heap (smaller values have higher priority).
* capture a photo of your final min heap
* Using a new sticky note, write down a small number.  This number does not need to be smaller than the smallest value but it needs to be either smallest, second smallest or third smallest value in your heap.
* Insert this last value but as you do it, photograph its movement for the insertion process. (a photo for each step, including where you start, then where it goes, until where it finds its final spot).  Please make sure to add the photos in the appropriate order to lab5.md.

### Part B: Heap removal

* As a group review the process of removing the highest priority item in a heap
* Have each member perform one removal operation from the heap you built in the Part A
* Photograph what your heap looks like after each removal operation.

Answer the following question:

* What values did you remove? (write these out in the order that they were removed)


### Part C: Array Representation of heap.

While we picture a heap as a tree, it is actually stored as an array. Pick one of the photographs you captured during the heap removal process and write down the array representation of that heap.


### Part D: Creating a heap in place

Place your sticky notes in random ordering in a row... if you can't fit it into the whiteboard you can put sticky notes on the wall (but obviously don't write on the wall). Your array should have 11 numbers in it.  If you are missing numbers, create more numbered sticky notes and add them to the array so that you have 11 numbers

Create a duplicate set of sticky notes (copy all values of originals into another sticky)

Form the complete binary tree using this second set of sticky notes so that it matches your array.

Photograph your tree and associated array.  

Look at the nodes in your tree, starting at the bottom right most node, work your way left and up until you find the first non-leaf node.

Answer the following questions:

* What number is the first non-leaf node starting from bottom?
* What index is that node at?


Repeat the process below until you reach the first value in the heap, take turns doing this and explain what you are doing as you go.
- Starting at the first non-leaf node (the one you identified earlier), identify the subtree that uses that non-leaf node as root of tree and draw a triangle around the nodes of that subtree
- Turn that subtree into a **max_heap** by performing the heapify algorithm on the heap.  Ensure that the array and tree match
- Go to value one index lower (closer to front of array) and repeat above process.  That is, identify new subtree, repeat heapify algorithm

photograph the final tree after heapifying the tree.

### Part E: Heap Sort

Once you have part D completed you should have a **maxheap**

a) Check that your heap is a heap and a maxheap..If it is not, redo part D
b) ensure that your tree representation and array representation match

Before you do anything else answer the following questions:

1) how many values are in your array?
2) what is index of last value in array?

Once you are certain you have a max heap, perform a single removal operation on your heap, ensure that you are also adjusting your array

1) what was the first value removed? How does this number compare with others in heap (biggest? smallest?)
2)  Look at your heap portion of the array after you did this removal.. how many values are in it, what is the index of the bottom right most value in heap?

Place the removed value at end of your array but don't change your tree...  Just ignore this number and leave it at the end.

1) Perform another remove from the heap and adjust the array to match
2) What was the second value removed and how does it compare with others still in heap?
3) Look at your heap portion of the array after you did this removal.. how many values are in it, what is the index of the bottom right most value in heap?
4) Are there any open spots in the array that is not part of the heap and not holding anything useful?


Place the removed value into the opens spot but don't change your tree.

1) Perform another remove from the heap and adjust the array to match
2) What was the second value removed and how does it compare with others still in heap?
3) Look at your heap portion of the array after you did this removal.. how many values are in it, what is the index of the bottom right most value in heap?
4) Are there any open spots in the array that is not part of the heap and not holding anything useful?
