def count_squares(width, height, size):
    if size <= 0 or width <= 0 or height <= 0:
        return 0

    squares_in_width = width // size
    squares_in_height = height // size
    return squares_in_width * squares_in_height

width = int(input("Введите ширину: "))
height = int(input("Введите высоту: "))
size = int(input("Введите сторону: "))

result = count_squares(width, height, size)
print("Количество квадратов: ", result)
