C = 'a'
A = ["apple", "banana", "ana", "aa", "a", "level", "car"]

count = sum(1 for s in A if len(s) > 1 and s.startswith(C) and s.endswith(C))

print("Количество подходящих элементов:", count)