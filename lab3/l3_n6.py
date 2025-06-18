def multiplication_numbers(numbers):
    count = 1
    for i in range(1, len(numbers), 2):
        count *= numbers[i]
    return count

numbers_list = [2, 3, 5, 7, 11, 13]
result = multiplication_numbers(numbers_list)
print(f"Произведение чисел на нечетных местах: {result}")
