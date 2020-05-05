k, n, w = map(int, input().split())
total = 0
for i in range(1,w + 1):
	total = total + i * k

print(total - n) if total >= n else print(0)

	
