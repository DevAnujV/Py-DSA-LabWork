# Analysis and Reflection for Lab 1

## function 1:

Analyze the following function with respect to number

```python
def function1(value, number):
	if (number == 0): #1
		return 1
	elif (number == 1): #1
		return value #1
	else:
		return value * function1(value, number-1) #1+ T(n-1)
		
		# for 1st time - T(1) = T(n-2) + 6
		# for 2nd time - T(2) = T(n-3) + 9
		# for K times  - T(K) = T(n-(K+1) + 3K+3
		# for T(1) we know that it is 3 because 3 operation taking place (==0 , ==1 and return)
		# In out equation T(1) means that,  n-(K+1) = 1, means - K = n-2
		# Substituting the values -
		# T(n) = T(1) + 3(n-2) + 3
		# 3 + 3n - 6 + 3
		# 3n
		# Hence, T(n) = 3n means O(n)
```

## function 2:

Analyze function2 with respect to the length of the mystring.  Hint, you will need to set up two mathematical functions for operator counting.  one for function2 and the other for recursive_function2

```python

def recursive_function2(mystring,a, b):
	if(a >= b ): #1
		return True
	else:
		if(mystring[a] != mystring[b]): #1
			return False
		else:
			return recursive_function2(mystring,a+1,b-1)  #1+1+1+(T/2)

def function2(mystring):
	return recursive_function2(mystring, 0,len(mystring)-1) # 3 (fuction call, len, and - operator)

# Here because the recursive call will always get to n/2 of the string length. Because lets say we have 10 length of string. Once it reaches 5, a = b, which is base case. Hence, T(n) = O(n/2)
```

### function 3 (optional challenge):

Analyze the following function with respect to number


```python
def function3(value, number):
	if (number == 0):
		return 1
	elif (number == 1):
		return value
	else:
		half = number // 2
		result = function3(value, half)
		if (number % 2 == 0):
			return result * result
		else:
			return value * result * result

```

## Part C reflection

Answer the following questions

1. Describe how to a approach writing recursive functions, what steps do you take?

- Identify the base case - this is the simplest scenerio when function ends or do not makes a call to itself again.
- Identify a simple recursive case - Find a simple recursive solution for the same problem. for eg- for an easy or smaller case.
- Rely on recursive leap of faith. If the solution work for small problem, it will work for bigger problem as well.
- Make sure that after each call to recursive function, we are going towards the base case i.e. closer to solution.
- run and debug if any errors occured.

2. Describe the process of analyzing recursive functions.  How does it differ from from analyzing non-recursive functions?  How is it the same? 

- Analysis of recursive function is not that much different from non-recursive function. Same methodology will be used to find a 
formula that will give us number of operation required. Let T(n) be the number of operations taken to find that. Similar to non-recursive function , we will count our opertions. For example, +, -, > or <, etc. The only difference is here the function is calling itself again. Lets say, function is calling with n-1 value to be passed. Its T(n) will be all the constants + T(n-1)
After some more calls, it will be reducting itself to n-2, n-3, etc and will give us with more constants. Till we get to our base condition. Before that, we can get to an intermediatory position, lets say after K calls. After K calls, T(K) = c + T(n-K)
And for base condition, n-K = 0 or n=K. Then we can substitute the values and finally get an equation and drop the constants and we can get T(n) in terms of BigO.
