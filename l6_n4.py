numbers = [ -5, -3, -1, 2, 4, -2, 6, 8, -7 ]

first_positive = next((num for num in numbers if num > 0), None)

last_negative = next((num for num in reversed(numbers) if num < 0), None)

print("Первый положительный элемент:", first_positive)
print("Последний отрицательный элемент:", last_negative)