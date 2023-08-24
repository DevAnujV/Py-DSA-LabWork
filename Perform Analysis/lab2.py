
def fibonacci(number):
	
	if (number < 2):
		return number;

	return fibonacci(number-1) + fibonacci(number-2);

    # x = 0;
    # y = 1;
    # z = 0;

    # for p in range(number):
    #     if (number <= 1):
    #         return number;
    #     else:
    #         z = x+y;
    #         x = y;
    #         y = z;
    
    # # print(anotherNum);
    # return x;

                     



def sum_to_goal(numList, goal):
	# for x in range(len(numList)):
	# 	for y in range(x+1, len(numList)):
	# 		if (numList[x] + numList[y] == goal):
	# 			return numList[x]*numList[y];
	# return 0;
    dict = {};
    for i, j in enumerate(numList):
        diff = goal - j
        if (diff in dict):
            return (diff* numList[i]);
        dict[j] = i
    return 0;




    