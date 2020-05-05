def swapper(n, t, arr):
	for i in range(t):
		
		i = 0
		while(i < n-1):
			if arr[i] != arr[i + 1] and arr[i] == "B":
				arr[i], arr[i+1] = arr[i + 1], arr[i]
				i += 2
			else:
				i+=1
	return "".join(arr)
				


n, t = map(int, input().split())
string = input()
string_list = list(string)

print(swapper(n,t, string_list))
