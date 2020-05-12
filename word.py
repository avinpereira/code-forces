s = input()
count_lower = 0
count_higher = 0
for i in s:
	if i.islower():
		count_lower += 1
	else:
		count_higher += 1
if count_lower >= count_higher:
	print(s.lower())
else:
	print(s.upper())
	
