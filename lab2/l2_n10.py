my_list = []

print("Введите элементы для добавления в список (для завершения введите пустую строку) ")

while True:
    element = input("Введите элемент: ")

    if element == "":
        break

    my_list.append(element)

print("Список: ", my_list)
