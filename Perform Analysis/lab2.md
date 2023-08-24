# Lab 2


### function 1:

Analyze the following function with respect to number

```python
def function1(number):
	total=0;  # 1

	for i in range(0,number): #number times + 1
		x = (i+1) # 2(number)
		total+=(x*x) # total = 3(number)

	return total # 1

	# T(n) = 1 + n+1 + 2n + 3n + 1
	# T(n) = 6n+3
	#T(n) = remove constants so becomes O(n)
```

### function 2:

Analyze the following function with respect to number

```python
def function2(number):
	return  ((number)*(number+1)*(2*number + 1))/6 # 2+1+1+1+1 = 6

	#Here it is constant since T(n) = O(1)
```

### function 3:

Analyze the following with respect to the length of the list.  Note that the function call len() which returns the length of the list is constant (O(1)) with respect to the length of the list.
```python

def function3(list):
	for i in range (0,len(list)-1): #n + 1 + 1 + 1
		for j in range(0,len(list)-1-i): # n(1+1+1+1) 4n
			if(list[j]>list[j+1]): #2*(n^2)
				tmp=list[j] # n^2
				list[j]=list[j+1] # 2(n^2)
				list[j+1]=tmp # 2(n^2)

# T(n) = 3+n + 4n+ 7n^2 = 3+5n+7n^2
# Depends on the dominant value so n^2. Hence, T(n) = O(n^2)
```
### function 4:

Analyze the following function with respect to number

```python
def function4(number):
	total=1 #1
	for i in range(1 to number): #(n-1)+1
		total=total*(i+1) #3(n-1)
	return total #1

	 # T(n) = 1+(n-1)+1+3(n-1)+1
	 #T(n) = 4n-1
	 # T(n) = O(n)
```


## In class portion


### Group members
List the members of your group member below:

	* Name 
	* Yeseul Ju
	* Anuj Verma
	* Avni Goel
	* Sanya Khurana
	* Himshikha

### Timing Data
Note, if a groupmate did not complete lab1, simply put 0.0 in for the times, it is ok if there is something missing.

| Team member | Timing for fibonacci | Timing for sum_to_number | 
|---------------|--------|---------|
| Yeseul Ju     | 3.739  | 1.395   |
| Anuj Verma    | 1.6524 | 0.0025  |
| Avni Goyal    | 1.681  | 0.0027  |
| Sanya Khurana | 2.73   | 0.766   |
| Himshikha     | 0.0000138 | 0.50 |


### Summary 

| function     | fastest | slowest | difference
|--------------|---------|---------|-----------|
|sum_to_number | 0.0025  | 1.395    | 1.3925   |
|fibonacci     | 0.0000138  | 3.739 | 3.7389   |


### Discussion:

Look at the code from lab 1 and discuss the differences between fastest/slowest versions. Was it a difference in syntax? A difference in approach?  Write down your observations.

Ans - There was quiet a difference in both the fastest and the slowest version. For both Fibonacci and sum_to_number the time was different. Talking about fibonacci, all the functions mostly use recursion so the time difference is not much change. But for Himshika, she have used regular assignment approach. Her T(n) is O(n). So, it was faster. Moving further, sum_to_number approach was fastest for Anuj because, all the other functions are mostly using 2 for loops which makes T(n) = O(n^2). However, Anuj used one for loop and another hashmap (dictionary) because dictionary have T(n) = O(1) in most cases. So, its time complexity is O(n). Hence, it is working in faster way.

## Reflection

1. Considering the solutions you saw when looking at the lab 1 code, what differences did you see between fastest and slowest versions of code?

- The difference b/w the fastest and slowest version of code is mostly the approach. For example, in the sum_to_array function, the slowest version is doing that with 2 for nested loops. First, one loop is ran, then second loop is ran, it will first check the first element with all the other element to see if the sum exists. Then, second element with all the element and so on. Fastest function, on the other hand, is running the loop just once and finding the difference first (element-target) and is checking if the difference exist in the whole array (a hashmap (dictionary) is created of this array). and then, once the difference is found in the dictionary, that element is returned along with the previouly stored value in dictionary. Hence time complexity for this function is T(n) = O(n) as oppose to O(n^2).

2. Was there a difference in terms of usage of space resource?  Did one algorithm use more/less space (memory)?

- Yes, there was quiet a difference in the usage of space resource. First of all, when recursion is used for the fibonacci, it used a way more stack memory and one the other hand, using range for and assingment (faster approach) is using way less stack memory. Similarly, sum_to_number function, the faster version is using more space resourcre because, a dictionary is being created where I am pushing all the element from the array, till we found the sum. But, other functions (slower) uses nested for loops and just returns products of two numbers once matched.


3. What sort of conclusions can you draw based on your observations?
- From these observations, I came to know that, recursion is not always the best way to solve a problem as it can cost more space and time. Because, the fastest version is not done with recursion. Moving further, nested for loops for sum_to_goal function, time complxtiy is O(n^2) which is more time consuming than O(n) (faster version) that uses one for loop an a dictionary whose T(n) is 1 or constant.

