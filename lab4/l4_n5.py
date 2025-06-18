try:
    num1 = float(input("Введите делимое: "))
    num2 = float(input("Введите делитель: "))
    result = num1 / num2
    print("Ответ: ", result)

except ZeroDivisionError:
    print("Делить на ноль нельзя")
except ValueError:
    print("Введено не число")
