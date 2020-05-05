a , b = input().split(' ')
a , b = int(a), int(b)

year = 0
while(a <= b):
    year+=1
    a*=3
    b*=2

print(year)
