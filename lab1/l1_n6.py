def season_events(number_of_month):
    month = str()
    if number_of_month == 1:
        month = 'Январь'
        print("Вы родились в", month, '-', 'За окном падал белый снег')
    elif number_of_month == 2:
        month = 'Февраль'
        print("Вы родились в", month, '-', 'За окном падал белый снег')
    elif number_of_month == 3:
        month = 'Март'
        print("Вы родились в", month, '-', 'Птицы пели прекрасные песни')
    elif number_of_month == 4:
        month = 'Апрель'
        print("Вы родились в", month, '-', 'Птицы пели прекрасные песни')
    elif number_of_month == 5:
        month = 'Май'
        print("Вы родились в", month, '-', 'Птицы пели прекрасные песни')
    elif number_of_month == 6:
        month = 'Июнь'
        print("Вы родились в", month, '-', 'Солнце светило ярче чем когда-либо')
    elif number_of_month == 7:
        month = 'Июль'
        print("Вы родились в", month, '-', 'Солнце светило ярче чем когда-либо')
    elif number_of_month == 8:
        month = 'Август'
        print("Вы родились в", month, '-', 'Солнце светило ярче чем когда-либо')
    elif number_of_month == 9:
        month = 'Сентябрь'
        print("Вы родились в", month, '-', 'Урожай был невероятным')
    elif number_of_month == 10:
        month = 'Октябрь'
        print("Вы родились в", month, '-', 'Урожай был невероятным')
    elif number_of_month == 11:
        month = 'Ноябрь'
        print("Вы родились в", month, '-', 'Урожай был невероятным')
    elif number_of_month == 12:
        month = 'Декабрь'
        print("Вы родились в", month, '-', 'За окном падал белый снег')
    else:
        print("Такого месяца не существует")


number = season_events(int(input("Введите реальный номер месяца вашего рождения: ")))
