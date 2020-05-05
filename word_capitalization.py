


string = input()
result = ""
for i in range(len(string)):
	if i == 0:
		result = result + string[i].capitalize()
	else:
		result = result + string[i]

print(result)
