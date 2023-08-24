
1. What sorting algorithm was the speaker trying to improve?

-> Speaker is trying t improve the heap sort algorithm because its average and worst case takes the same time because it shuffles all the elements sorted or not.

---
2. At what partition size does VS perform a simpler sort algorithm instead of continuing to partition?

-> 32

---
3. At what partition size does GNU perform a simpler sort algorithm instead of continuing to partition?

-> 16

---
4. Regular insertion sort does a linear search backwards from end of array for correct spot to insert.  According to the speaker, why does switching to a binary search not improve performance?

-> Because of predictibility and entropy. Althought the number of comparisons will be less for binary search. However, due to  uncertainity, the branch predictor will be having a hard time figuring out what will be the less so the chances will reduce to 50% to get everything right and hence more time will be invested. So, binary search is not better in insertion sort.

---
5. Describe what is meant by branch prediction? (this may require further research)

-> Branch prediction is a technique used in computer processors to optimize the execution of conditional branch instructions in a program. In modern processors, conditional branches are a common occurrence in program code, and they often introduce a potential performance bottleneck due to their unpredictable nature.

---
6. What is meant by the term **informational entropy**? (this may require further research)

-> In information theory, entropy is used to analyze and quantify the amount of information in a message or data stream. The more unpredictable or uncertain the data is, the higher its entropy. Conversely, if the data is highly predictable or follows a specific pattern, the entropy is low.

---
7. If size == 15, what is size & 1?  if size == 16, what is size & 1?  Explain how right = first + 1 + (size & 1) avoids a conditional check.

	Hint:
	* The & is the bitwise AND operator in C/C++.  It takes the bit representation of the two operands and perform an AND operation on each of the corresponding bits to form a result
	* To do this question first convert 15, 16 and 1 to base 2 (use 5 digit representation for all of them).  Then perform an AND operation of the correseponding bits of the operands... this will get you a 5 digit binary value.  Convert the value back to base 10 .

-> size = 15:
Binary representation of 15: 01111
Binary representation of 1: 00001
So, size & 1 evaluates to 1 when size is 15.
size = 16:
Binary representation of 16: 10000
Binary representation of 1: 00001
Performing bitwise AND:
So, size & 1 evaluates to 0 when size is 16.
If size is odd, size & 1 evaluates to 1, so right becomes first + 1 + 1, which effectively adds 1 to right (when size is odd).

If size is even, size & 1 evaluates to 0, so right becomes first + 1 + 0, which is the same as right = first + 1, effectively not adding anything extra to right (when size is even).
Therefore, the expression right = first + 1 + (size & 1) handles the condition of odd or even size without explicitly using an if-else statement. By using the bitwise AND 
operator &, it efficiently determines whether to add the extra value (1) to right 
---

8. Speaker suggests the following algorithm:
	* make_heap()
	* unguarded_insertion_sort()

	He suggests that by doing make_heap() first then you can do something called unguarded_insertion_sort().  Explain what is unguarded_insertion_sort() and why it is faster than regular insertion sort.  How does performing make_heap() allow you to do this?

-> When we create a min-heap using make_heap(), the smallest element of the array is already at the root. By repeatedly swapping the root with the first unsorted element and restoring the min-heap property, the smallest elements "bubble up" to the start of the array. This is similar to how the regular insertion sort places the smallest element at the correct position in each pass. The difference is that unguarded insertion sort performs this operation more efficiently due to the use of a heap.

---
9. The speaker talks about incorporate your conditionals into your arithmetic.  What does this mean?  Provide an example of this from the video and explain how the conditional is avoided.

-> Incorporating conditionals into arithmetic" refers to the practice of using mathematical operations to achieve the same result as a conditional statement, thereby avoiding the need for explicit if-else checks in the code
It is helpful because it will lead to more concise and efficient code.
Example - 
auto right = first  + 1 + (size & 1)
This means that if the size is even then it comes to 1 (true) and right is one incremented.
If the size if odd - then the condition becomes false because odd & 1 is 0, hence not incremented.
It is same as if else.

---
10.  The speaker talks about a bug in gnu's implementation.  Describe the circumstances of this bug.

-> In the GNU implementation, there is a test for a lone child which is being done using an outer loop. Mkae a heap without last element and then use push heap to put that
last element with log n cost.

---
11.  The speaker shows several graphs about what happens as threshold increases using his new algorithm.  The metric of comparison is increased, the metric of moves are increased but time drops... What metric does the author think is missing?  Describe the missing metric he speaks about in the video.  What is the metric measuring?

-> The metric the creator believes is missing is when time proceeds to drop and the correlation increments is Gather D(n), normal distance between two resulting cluster gets to. This measurement will give store without really having a reserve explicit metric since it will return and show that it doesn't work since it gives various closures of the exhibit. Alexandrescu then, at that point, took a gander at the distance for quicksort and it's extremely huge since it begins at the most pessimistic scenario for dividing. He then, at that point, takes a gander at D(n) and takes a gander at the chart however the two measurements are as yet going down. His answer is to construct a composite metric that envelops the entirety of the three execution so you'd have a mixed expense of your calculation. The measurement is for working on arranged calculations.
---
12.  What does the speaker mean by fast code is left leaning?

-> According to Alexandrescu, when discussing "fast code being left leaning," he suggests that if you want your code to be fast, it should be positioned towards the left side of the page. When we analyze the structure of code, such as if statements, for loops, switch statements, and other decision points, it becomes evident that they can create loops, leading to inefficiencies in the code's performance. To achieve speed, code should lean left because it aims to avoid mixing hot and cold operations.
---
13.  What does the speaker mean by not mixing hot and cold code?

-> Alexandrescu refers to "hot and cold code" as an "inefficiency anti-pattern" that can be avoided. The optimal approach involves grouping hot code together and cold code together. Hot code represents critical parts of the code that are frequently executed, like breaking out of a loop and returning. In contrast, cold code, often considered "fix-up," is less important and less frequently accessed. By organizing code in this manner, we can improve overall efficiency and performance.


## Reflection:

1. What did you/your team find most difficult to understand in the video?

-> The most difficult thing that I find to understand in this video is understanding the unguarded_insertion_sort(). It basically is based on the idea that once the min heap is formed, we do not have to do a bounce check to redo it becuase the 1st element will be always smaller than the next element.

2. What is the most surprising thing you learned that you did not know before?

-> There are various new things that were fascinating to me that I was not exposed to previously. One of them being different and better sorting techniques like unguarded insertion sort, etc, Various terms like branch prediction, informational entropy.
Also how in the back end with the prediction and repition of logic, computer is able to do the same work with much more efficiency and speed as compared to unpredicted data. Also, I got to learn to avoid the condiitonal statements and incorporate the conditionals with arithematics, etc.

3. Has the video given you ideas on how you can write better/faster code?  If yes, explain what you plan to change when writing code in the future.  If no, explain why not.

-> Yes, this video have definitely helped to improving the coding skills. There are alot of points to take care for eg taking care of hot and cold code as mentioned abobve, incorporating the conditionals with arithematics and avoid conditional statements which will improve the efficiency of the code. Moroever, there are also very neat sorting algorithms that author proposed which significantly improves the efficiency furhter, Hence, there was alot of high advance things to learn from this video.




