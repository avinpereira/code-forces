n = int(input())
count = 0
max_req = 0
for i in range(n):
	pass_in, pass_out = map(int, input().split())
	count -= pass_in
	count += pass_out
	if count > max_req:
		max_req = count

print(max_req)
