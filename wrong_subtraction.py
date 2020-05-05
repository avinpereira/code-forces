
def wrong_subtraction(n,k):
    # import pdb; pdb.set_trace()
    i = 0
    result = n
    while (i < k):
        if result % 10 == 0:
            result = result / 10
        else:
            result = result - 1
        i+=1
    return int(result)

n , k = input().split(' ')
n , k = int(n), int(k)
print(wrong_subtraction(n,k))

# class TestCompressor(unittest.TestCase):

#     def test_10_Once(self):
#         assert wrong_subtraction(10,1) == 1

#     def test_100_1(self):
#         assert wrong_subtraction(100,1) == 10

    

# if __name__ == '__main__':
#     unittest.main()