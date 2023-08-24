# Lab 7


* Anuj Verma
* Avni Goyal

## Part A: BST Insert

As a group review bst insertion algorithm.

* Take one photo of the original row of sticky notes
![image](https://github.com/seneca-dsa456/averma100/assets/113152048/455528c8-084b-44a0-88f2-4cee2c81bfbc)


* When completed, take one photo of the final tree
![image](https://github.com/seneca-dsa456/averma100/assets/113152048/274cd82e-0989-4aa6-81f3-0f488ab1475f)


Answer this question.

* What is the height of your final tree?
7

## PART B: BST Deletion

* Find a node in your tree with 2 children and remove that node.
	* Take a picture of tree
 * ![image](https://github.com/seneca-dsa456/averma100/assets/113152048/3031e63b-0253-4145-8c4d-b3059ac00f57)


* find another node with 2 children and remove that node
	* Take picture of tree
 * ![image](https://github.com/seneca-dsa456/averma100/assets/113152048/f2ede451-5f31-4486-94b9-31684fe1ddec)


* remove the root node of the tree
	* take picture of tree
![image](https://github.com/seneca-dsa456/averma100/assets/113152048/4d201d3f-4525-4061-afee-04985f140d9f)


Answer this question:

* Anytime you remove a node with 2 children, you need to find a node to take over for node being removed.  Explain how you found your replacement.
- Everytime a node is removed the replacement is found by finding the next predicessor of its parent by going to right and then going extreme left.
- This way predecessor can be found and we have to make the parent of the removing node point to the predecessor.

## Part C AVL


* Take one photo of the original row of sticky notes
* ![image](https://github.com/seneca-dsa456/averma100/assets/113152048/231723b4-50e3-4c9b-a534-197b34af12fa)


* When completed, take one photo of the final tree
* ![image](https://github.com/seneca-dsa456/averma100/assets/113152048/c2849d46-dfaa-411b-afb2-ff7b6ba3c3b2)

Answer these questions. 
* How many times you had to do a single rotation?
  2
* How many times you had to do a double rotation?
  2
* How tall is your final tree?
  5

## Part D Red-black trees (optional)

## Part E 2-3 trees


* Take one photo of the original row of sticky notes
  ![image](https://github.com/seneca-dsa456/averma100/assets/113152048/a02bd592-2f3b-458e-bd9e-8dfca89e4b07)


* When completed, take one photo of the final tree
  ![image](https://github.com/seneca-dsa456/averma100/assets/113152048/cb64500a-2ba8-4693-8cfd-62e16b85ea57)


* How many times did you split?
6 splits

## Part F Dijkstra's Algorithm

![Graph](https://user-images.githubusercontent.com/1699186/203682880-1f8d6068-3668-4b2c-9abe-40cb79294177.png)

Use Dijkstra's algorithm to find the shortest distance from vertex A to every other vertex.  Show your work by creating the table below:

![image](https://github.com/seneca-dsa456/averma100/assets/113152048/a2b28aef-d7ae-47c7-b82e-8eb4a966f343)
![image](https://github.com/seneca-dsa456/averma100/assets/113152048/a4fff794-f0b8-4ef0-9431-4574e50dc05e)
![image](https://github.com/seneca-dsa456/averma100/assets/113152048/8b05da6e-97d8-4c9e-998b-4c35b6de672e)


Result summary: Fill in the final result in this table.  For path list all nodes for example, if you are going from A to B to C to D, then path is A-B-C-D


| Vertex | Path | Distance to A|
|---|---|---|
| A  |  - | 0 |
| B  |  A-B | 5 |
| C  |  A-B-C | 9 |
| D  |  A-B-C-D | 11 |
| E  |  A-F-E | 10 |
| F  |  A-F | 3 |
| G  |  A-B-C-D-G | 12 |


## Part G: Reflection

This last part is to be completed individually.

Write a short paragraph about what you learned from this lab.
- I have alearned alot from this lab. First of all, BST trees, the way the insertion in binary search tree happens, smaller than parent goes to left and bigger to the right. It makes much more sense after drawing it. Moving on, deleting nodes from BST was also interesting. On deleting, we have to see which is the next predecessor of the parent of the node which is being deleted by going to one right and then extreme left to the node that is being deleted. Thsi way we can find the next one and make the parent of node to be deleted point to that. Moving on, AVL tress was another interesting concept. It was basically concept of self balancing trees. Which it meant is that a tree is balanced when its each node have the balancing index of -1, o or +1. It is calculated by subtracting left subtree height from the right. If ever the index falls out of range we have to do a rotation. If the index is out of range and the sign is opposite, we have to do a double rotation. Moving on, then came the concept of 2-3 trees. This was an amazing concept. It worked on the principle that, a node can have either 1 or 2 value. Addional value will cause the node to spilt with the median of those 3 values becomming the parent and rest 2 as children. THen when we have to add new value, the concept is same as of BST, it will add to left or right but it will add to the same node not making the parent. So, till that node become 3, then it will split promoting median to the parent. And once the parent becomees 3, then it will again split, hence we will always have a balanced tree. Also keep in mind that the new value comming is compared with the two parent values and based on if it is less greater or in the middle it will follow the left, right or middle path and hence be the pare of that node (out of 3 children). Lastly, Dijkstra's algorithm to find the shortest distance from a node to all other nodes. Different tables were created and we explore one node and mark it true and then follow the minimum distance node and explore that and mark it true and go on. It is done till all the nodes are explored and then we will have our final answer.
That was all for this assignment.

