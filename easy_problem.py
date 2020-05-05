# def is_hard(l):
#     for i in l:
#         if(i == 1):
#             return "HARD"
#     return "EASY"


def is_hard(l,p):
    sorted_list = sorted(l)
    if sorted_list[p - 1] == 0:
        return "EASY"
    return "HARD"

people = int(input())
response_list = [int(x) for x in input().split(' ')]

print(is_hard(response_list, people))



