




size = int(input())
string = input()

bool_arr = [False] * 26

for i in string.lower():
	index = ord(i) - 97
	bool_arr[index] = True

check = True
for i in bool_arr:
	if i is False:
		check = False
		break

if check:

	
	print("YES")
else:
	print("NO")
