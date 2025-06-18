def positive_number(array):
    count_numbers = 0
    for i in array:
        if i > 0:
            count_numbers += 1

    print("Количество отрицательных чисел: ", count_numbers)

positive_number([1, 15, -25, -2, -8, 14])