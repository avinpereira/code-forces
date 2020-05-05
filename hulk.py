def hulk(n):
    i = 1
    result = ""
    while(i <= n):
        if(i == n and i % 2 == 0):
            result+="I love it"
            return result
        elif (i == n and i % 2 != 0):
            result+="I hate it"
            return result
        #i is odd
        elif(i % 2 != 0):
            result+="I hate that "
        else:
            result+="I love that "
        i+=1






n = int(input())

print(hulk(n))

