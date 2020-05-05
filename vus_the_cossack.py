def find_enough_gifts(n,p,b):
	if p >= n and b >= n:
		return "Yes"
	return "No"





n,p,b = map(int, input().split())
print(find_enough_gifts(n,p,b))
