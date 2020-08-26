string1 = input()
string2 = input()
mixture = input()
bit_vector = [False] * 26
for i in string1:
	index = ord(i)
	index = index - 65
	bit_vector[index] = not bit_vector[index]

for i in string2:
	index = ord(i)
	index = index - 65
	bit_vector[index] = not bit_vector[index]

for i in mixture:
	index = ord(i)
	index = index - 65
	bit_vector[index] = not bit_vector[index]

switch = False
for i in bit_vector:
	if i:
		switch = True
		print("NO")
		break

if not switch:
	print("YES")
	
