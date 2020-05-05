def find_language(string):
	length = len(string)
	check = string[length - 1]
	if check == "o":
		print("FILIPINO")
	elif check == "u":
		print("JAPANESE")
	else:
		print("KOREAN")

















n = int(input())
for i in range(n):
	string = input()
	find_language(string)
