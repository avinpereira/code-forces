n, h = map(int, input().split())
heights = [int(x) for x in input().split()]
width = 0
for i in heights:
	if i > h:
		width += 2
	else:
		width += 1

print(width)
 
