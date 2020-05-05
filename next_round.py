def next_round(arr, n, k):
	value_to_beat = arr[k - 1]
	count = 0
	for i in arr:
		if i >= 1 and  i >= value_to_beat:
			count+=1
	return count




n,k = map(int, input().split())
arr = [int(x) for x in input().split()]
print(next_round(arr, n , k))
