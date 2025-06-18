def largest(a, b):
    if a > b:
        print("Наибольшее число из", a, "и", b, "это ", a)
    else:
        print("Наибольшее число из", a, "и", b, "это ", b)

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
largest(a, b)
