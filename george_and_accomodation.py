n = int(input())
count = 0
for i in range(n):
	taken,capacity = map(int,input().split())
	if capacity - taken >= 2:
		count += 1
print(count)
