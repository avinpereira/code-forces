string = input()
string_without_bracket = string[1:len(string) - 1]
alphabets = string_without_bracket.split(', ')
my_set = set(str(x) for x in alphabets)
if my_set == {''}:
	print(0)
else:
	print(len(my_set))

