



n = int(input())
string = input()
i = 0
count = 0
while i < n - 1:
	if string[i] == string[i+1]:
		count += 1
	i += 1

print(count)

