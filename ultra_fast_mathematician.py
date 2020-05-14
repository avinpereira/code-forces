n1 = input()
n2 = input()

length = len(n1)
result = ""
for i in range(length):
	if int(n1[i]) ^ int(n2[i]):
		result = result + str(1)
	else:
		result = result + str(0)

print(result)


