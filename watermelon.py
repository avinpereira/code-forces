def is_dividable(n):
	if n < 4:
		return "NO"
	if n % 2 == 0:
		return "YES"
	return "NO"







n = int(input())
print(is_dividable(n))
