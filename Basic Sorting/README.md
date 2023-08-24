## Objectives:

- Learn how sorting works
- Practice communicating and working together as a team.  This is an essential skill for software developers.  Techniques such as [Pair Programming](https://en.wikipedia.org/wiki/Pair_programming#Learning) require you to communicate effectively.


## Learning to sort:


### The Simple Sorts

* As a group review the algorithms for bubble sort, insertion sort and selection sort
	https://seneca-ictoer.github.io/data-structures-and-algorithms/D-Searching-And-Sorting/simple_sorts

* Assign one of these sort to each team member. (for teams of two work together on the last one)
* Each team member will demonstrate how their assigned sort works using their 16 pieces of numbered paper.
	* lay out all 16 pieces of paper on table in front of you in a row
	* perform the sorting algorithm on the paper to sort them ascendingly
* Help each other out on this, correct misconceptions as you go through the sorts.  This is how it would go if you are programming together... do not assume that the person typing is correct. 
* As a group discuss the following and note it in your lab4.md file
	* which algorithm did you find the easiest to understand?
	* which algorithm seemed to be the fastest for completing the sort?


### Merging lists

For teams of two pick up an extra set of numbers from your prof.  Make sure its different coloured than the ones you have.

#### Merging unsorted lists

* have each member of the group lay out their papers in a row but keep them unsorted... that is you should have 3 rows of 16 number each.  All easily visible but not sorted
* have one member start a timer on one of their devices (phone, computer.. doesn't matter)
* have the other members try to create one new merged list by picking out the smallest values.
* Note the following in your lab4.md file
	* how long did this take
	* did you make any mistakes along the way (did you choose the wrong number and had to move things around)?
		* How many times? 

#### Merging sorted lists

* repeat the above but instead of laying out the papers in 3 unsorted rows, sort each row first.  That is you should have 3 rows of 16 numbers, in sorted order
* repeat this merging and time how long it took.
* Note the following in your 
	* how long did this take
	* did you make any mistakes along the way (did you choose the wrong number and had to move things around)?
		* How many times? 

### Lists Partitioning

For teams of two, use all 3 sets of numbers.

#### Sorting many numbers

* Take all the number papers for your team and mix it up forming a pile of numbered papers
* Have each team member sort all the papers however they like and time the result (mix up the numbers after each round so that everyone starts with randomly ordered values)
* Record how long it took each team member to get them sorted
	* Record the fastest time
	* Describe how the team member sorted them


### Partitioning

* Take all the numbers for your team and mix it up again
* partition the pile:
	* Time how long this process takes
	* have someone pick a random paper to serve as the "pivot" put that paper on table clearly away from pile
	* go through pile and place all numbered papers that are smaller to the left of the pivot, and all bigger to the right of the pivot.  These can still be piled up.
	* repeat one more time with these two smaller piles (unless there were 5 or few papers in the pile, in which case apply the patition only to the bigger half, then out of the two new piles apply the partitioning one more time to the bigger one, if they are about the same, pick any one and do it.)
* If this was correctly done, you should end up with 4 piles of numbers separated by 3 pivots  (it is possilbe to have empty piles.)  This is fine..it means you have one less pile to deal with in the next step.
* Record how long did the partitioning took


### Sorting small piles

* At this point, have the fastest sorter in your team separately sort each of the little piles. 
* By doing this, you should have a fully sorted set of numbers
* Record how long it took to do this


## Come up with the fastest way to sort

* As a team discuss things that helped sort the papers... what was useful? what was fast to do?  What was slow?
* As a team come up with a description of how best to sort a set of numbers on paper.
* Mix up all your numbers and have each member of the team perform the sort you did.  How long did it take?
