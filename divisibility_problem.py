
def is_divisible(a, b):
	if b == 0:
		return 0
	if a % b == 0:
		return 0
	factor = a // b
	next_divisible = (factor+1) * b
	count = next_divisible - a
	return count





t = int(input())
for i in range(t):
	a, b = input().split(' ')
	a = int(a)
	b = int(b)
	print(is_divisible(a, b))
