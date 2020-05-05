def restore_numbers(arr):
    largest = 0
    sum1 = 0
    sum2 = 0
    sum3 = 0
    for i in arr:
        if i > largest:
            if sum1 == 0:
                sum1 = largest
            elif sum2 == 0:
                sum2 = largest
            else:
                sum3 = largest
            largest = i
        elif sum1 == 0:
            sum1 = i
        elif sum2 == 0:
            sum2 = i
        else:
            sum3 = i
    output_string = ""
    output_string += str(largest - sum1) + " "
    output_string += str(largest - sum2) + " "
    output_string += str(largest - sum3) + " "


    # # Sorting Approach - takes longer
    # sorted_array = sorted(arr)
    # arr[0] = sorted_array[3] - sorted_array[0]
    # arr[1] = sorted_array[3] - sorted_array[1]
    # arr[2] = sorted_array[3] - sorted_array[2]
    # arr.pop(3)
    # for i in arr:
    #     output_string = output_string + str(i) + " "

    return output_string

        











arr = [int(x) for x in input().split(" ")]
response = restore_numbers(arr)
print(response)