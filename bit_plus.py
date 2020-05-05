def bit_operation(arr):
	x = 0
	for string in arr:
		if string[0] == "+" or string[2] == "+":
			x += 1
		else:
			x -= 1
	return x


n = int(input())
arr = []	
for i in range(n):
	arr.append(input())
print(bit_operation(arr))
