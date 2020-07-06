'''
Problem is a bit more complicated than it first appears.

Question:
1. Get the Maximum value to index 0 
2. Get the Minimum value to index n - 1
3. Return the number of seconds required to achieve the above condition such that 1 swap = 1 second


Solution observations:
1. Once the max value is identified, it takes a number of (swaps) = (index of max value) , to get it to the 0th index
2. It takes n - 1 - i swaps for the minimum number at index i to be swapped to the n-1th index
3. In a scenario, where the min value is to the left of the max value, we need to reduce the number of swaps by 1, as there is a point of time, where both minimum value & maximum value themselves get swapped 

'''






n = int(input())
arr = [int(x) for x in input().split(' ')]

max_value = arr[0]
max_index = 0
min_value = arr[n - 1]
min_index = n -1

for i in range(n):
	if arr[i] > max_value:
		max_value = arr[i]
		max_index = i
	if arr[i] <= min_value:
		min_value = arr[i]
		min_index = i
swaps = max_index
swaps += (n - 1) - min_index


if max_index > min_index:
	swaps -= 1

print(swaps)
	
