def find_matches(n):
	if n == 2:
		return 2
	if n % 2 == 0:
		return 0
	else:
		return 1




queries = int(input())
for query in range(queries):
	n = int(input())
	print(find_matches(n))

