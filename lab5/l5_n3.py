import random

def generate_array(length):
    array = [random.randint(0, 100) * 2 for _ in range(length)]
    array.sort()
    return array
