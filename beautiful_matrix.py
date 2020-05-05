def location(arr):
	for i in range(5):
		for j in range(5):
			if arr[i][j] == 1:
				return [i +1, j+1]



def beautify(arr):
	count = 0
	if arr[0] < 3:
		count = count + (3 - arr[0])
	elif arr[0] > 3:
		count = count + (arr[0] - 3)
	
	if arr[1] < 3:
		count = count + (3 - arr[1])
	elif arr[1] > 3:
		count = count + (arr[1] - 3)
	return count



arr = []
for i in range(5):
	row = [int(x) for x in input().split()]
	arr.append(row)

location = location(arr)
print(beautify(location))
