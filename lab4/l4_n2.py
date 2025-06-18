array = []
print("Введите 14 чисел ")
for i in range(14):
    number = int(input(f"Число {i + 1}: "))
    array.append(number)

sum_elements = sum(array)
array.append(sum_elements)
print("Массив: ")
for number in array:
    print(number, end= ' ')
