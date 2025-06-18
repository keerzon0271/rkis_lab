def divisor(a, b):
    return b % a == 0

a = int(input("Введите число а: "))
b = int(input("Введите число b: "))
print(f'{a} является делителем {b} - {divisor(a, b)}')