def get_year(n,t,list_n,list_t, year):
	result = ""
	if year > n:
		remainder = year % n
		result = result + list_n[remainder - 1]
	else:
		result = result + list_n[year - 1]
	
	if year > t:
		remainder = year % t
		result = result + list_t[remainder - 1]
	else:
		result = result + list_t[year - 1]
	
	return result

	





n , t = map(int, input().split(' '))
list_n = [x for x in input().split(' ')]
list_t = [x for x in input().split(' ')]
queries = int(input())


for query in range(queries):
	year = int(input())
	print(get_year(n, t, list_n, list_t, year))
