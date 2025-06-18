def task_2(array):
    sum_pos = sum(x for x in arr if x > 0)
    min_index = array.index(min(arr))
    max_index = arr.index(max(arr))
    start, end = min(min_index, max_index), max(min_index, max_index)
    product = 1
    for num in array[start + 1:end]:
        product *= num
    return sum_pos, product
