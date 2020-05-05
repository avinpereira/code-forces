def long(n):
	length = len(n)
	if length <= 10:
		print(n)
	else:	
		print( n[0] + str(length - 2) + n[length - 1])






n = int(input())
for i in range(n):
	string = input()
	long(string)
