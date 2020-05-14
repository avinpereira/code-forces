# The following logic is correct but test cases fail as time taken is more than 1 second

n = int(input())



#answer = 0
#
#for i in range(1, n+1):
#	if i % 2 != 0:
#		answer -= i
#	else:
#		answer += i


if n % 2 == 0:
	print(n // 2)
else:
	answer = -(n //2 + 1)
	print(answer)

