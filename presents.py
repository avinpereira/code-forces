n = int(input())
friends = [int(x) for x in input().split()]

dictionary = {}
for i in range(1, n + 1):
	dictionary[friends[i - 1]] = i

result = ""
for i in range(1, n + 1):
	result = result + str(dictionary.get(i)) + " "


print(result)
	

