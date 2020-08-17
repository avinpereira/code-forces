def count(home, away_count):
	count = 0
	for h in home:
		if h in away_count:
			count += away_count.get(h)
	return count 


n = int(input())


home = []
away_count = {}
for i in range(n):
	h, a = input().split(' ')
	home.append(h)
	if a in away_count:
		away_count[a] += 1
	else:
		away_count[a] = 1
print(count(home, away_count))
