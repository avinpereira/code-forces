
# Take the input as integer
n = int(input())

#A Loop that runs by incrementing n by 1 until a Unique number is found

while(True):
	my_set = set()
	n += 1
	string_number = str(n)
	for i in string_number:
		my_set.add(i)
	if len(my_set) == 4:
		break


print(string_number)
	
