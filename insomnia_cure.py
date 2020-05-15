k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())



my_set = set()

for i in range(k, d+1, k):
	my_set.add(i)

for i in range(l, d+1, l):
	my_set.add(i)
for i in range(m, d+1, m):
	my_set.add(i)

for i in range(n, d+1, n):
	my_set.add(i)

print(len(my_set))
	
