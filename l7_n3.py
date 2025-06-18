numbers = [ -5, 12, -3, 8, 0, -1, 15, -9, 4, 99, 10, -42 ]

two_digit_positives = sorted([num for num in numbers if num > 9 and num < 100])

print("Отсортированные двузначные положительные числа:", two_digit_positives)