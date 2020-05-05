def compare(string_1, string_2):
	length = len(string_1)
	for i in range(length):
		if string_1[i] == string_2[i]:
			continue
		if string_1[i] > string_2[i]:
			return 1
		else:
			return -1
	return 0






string_1 = input().casefold()
string_2 = input().casefold()

print(compare(string_1, string_2))
