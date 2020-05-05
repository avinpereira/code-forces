def love_a(string):
	length = len(string)
	counta = 0
	for i in string:
		if i == "a":
			counta += 1
	counto = length - counta
	
	removed = 0
	while((counto + counta)/2 >= counta):
		removed += 1
		counto -= 1	
	return length - removed









string = input()
print(love_a(string))
