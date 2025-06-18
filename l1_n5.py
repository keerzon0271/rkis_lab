def sieve(numbers):
    unique_numbers = set(numbers)

    reverse_list = list(unique_numbers)[::-1]

    return tuple(reverse_list)

my_list = sieve([1,2,3,4,5])
print(my_list)