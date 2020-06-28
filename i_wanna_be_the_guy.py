n = int(input())

arr1 = [int(x) for x in input().split(' ')]
arr2 = [int(x) for x in input().split(' ')]

arr1_count = arr1[0]
arr2_count = arr2[0]

my_set = set()
for i in range(1, n+1):
	my_set.add(i)

for i in range(1,arr1_count+1):
	if arr1[i] in my_set:
		my_set.remove(arr1[i])

for i in range(1, arr2_count+1):
	if arr2[i] in my_set:
		my_set.remove(arr2[i])

if len(my_set) == 0:
	print("I become the guy.")
else:
	print("Oh, my keyboard!")
