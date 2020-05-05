def retrieve_bills(amount):
    count = 0
    while(amount != 0):
        if(amount >= 100):
            quotient = amount // 100
            count += quotient
            amount = amount - (quotient * 100)
        elif(amount >= 20):
            quotient = amount // 20
            count += quotient
            amount = amount - (quotient * 20)
        elif(amount >= 10):
            quotient = amount // 10
            count += quotient
            amount = amount - (quotient * 10)
        elif(amount >= 5):
            quotient = amount // 5
            count += quotient
            amount = amount - (quotient * 5)
        elif(amount >= 1):
            quotient= amount // 1
            count += quotient
            amount = amount - (quotient * 1)
    return count





amount = int(input())

print(retrieve_bills(amount))

