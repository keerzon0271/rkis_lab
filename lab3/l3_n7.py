def check(numbers):
    p = numbers % 10
    n = numbers // 10
    while (numbers > 0):
        c = numbers % 10
        if c < p:
            return False
        p = c
        numbers = numbers // 10
    return True
print(check(54821))
print(check(765432))
