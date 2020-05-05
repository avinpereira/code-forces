def is_attempted(arr):
	counter = 0
	for i in arr:
		if i == 1:
			counter += 1
	if counter >= 2:
		return True
	return False




n = int(input())
counter = 0
for i in range(n):
	arr = [int(x) for x in input().split()]
	if is_attempted(arr):
		counter += 1

print(counter)
