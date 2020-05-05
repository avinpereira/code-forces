def domino(n,m):
	product = n * m
	return product // 2


n,m = map(int, input().split())
print(domino(n,m))
