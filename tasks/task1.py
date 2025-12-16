def sort_desc(arr):
    # сортирует массив по убыванию
    return sorted(arr, reverse=True)

def sort_asc(arr):
    # сортирует массив по возрастанию
    return sorted(arr)

def sum_arrays_with_zero(a, b):
    # складывает массивы; если элементы равны — результат 0
    return [0 if x == y else x + y for x, y in zip(a, b)]

def solve_task1(arr1, arr2):
    # решает задание 1 полностью
    if len(arr1) != len(arr2):
        raise ValueError("Массивы должны быть одинаковой длины")
    a_sorted = sort_desc(arr1)
    b_sorted = sort_asc(arr2)
    summed = sum_arrays_with_zero(a_sorted, b_sorted)
    return sort_asc(summed)