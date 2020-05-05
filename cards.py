
def get_binary(n, string):
	countz = 0
	countn = 0
	result = ""
	for i in string:
		if str(i) == 'n':
			countn += 1
		elif str(i) == 'z':
			countz += 1
	for i in range(countn):
		result = result + "1" + " "
	for i in range(countz):
		result = result + "0" + " "
	
	return result
		









n = int(input())
string = input()
print(get_binary(n, string))
