#
# Author: Anuj Verma
# Student Number: 180483216
#
# Place the code for your lab 3 here.  Read the specs carefully.  
# Function name must be exactly as provided.  
# Names of variables and parameters can be whatever you wish it to be
#
# To test, run the following command :
#     python test_lab3.py
#

def factorial(number):
	if (number <= 1):
		return 1;
	return number* factorial(number -1);


def linear_search(list, key):
	for i in range(len(list)):
		if (list[i] == key):
			return i
		
	return -1


def binary_search(list, key):
	beg = 0
	mid = 0
	end = len(list)-1
	
	while(beg <= end):
	
		mid = beg + int(((end - beg) / 2))

		if (key == list[mid]):
			return mid
		
		elif (key < list[mid]):
			end = mid -1
		else:
			beg = mid +1

	
	return -1