def is_pleasant(n, travel_string):
	s2sf = 0
	sf2s = 0
	for i in range(n - 1):
		if travel_string[i] == travel_string[i + 1]:
			continue
		elif travel_string[i + 1] == "S":
			sf2s += 1
		else:
			s2sf += 1
	
	if s2sf > sf2s:
		print("YES")
	else:
		print("NO")









n = int(input())
travel_string = input()
is_pleasant(n, travel_string)
