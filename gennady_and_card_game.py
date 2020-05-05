def check_if_move_exists(table, arr):

    for i in arr:
        if(table[0] == i[0]):
            return "YES"
        elif table[1] == i[1]:
            return "YES"
    return "NO"


table = input()
arr = [x for x in input().split(' ')]
print(check_if_move_exists(table,arr))

