def largest(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
print("Наибольшее из этих чисел это: ", largest(num1, num2))