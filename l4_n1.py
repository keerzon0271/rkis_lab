import random
array = []
for i in range(15):
    array.append(random.randint(0,100))

print("Массив: ")
for num in array:
    print(num, end= ' ')