def number_of_ways(number):
    max_leaders = number // 2
    ways = 0
    for i in range(1, max_leaders + 1):
        if (i == 1) or ((number - i) % i == 0):
            # print(i)
            ways += 1
    return ways









number_employees = int(input())
print(number_of_ways(number_employees))