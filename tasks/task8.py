def reverse_number(n):
    # возвращает перевёрнутое число
    return int(str(n)[::-1])

def count_common_with_reverse(arr1, arr2):
    """
    считает количество чисел из arr1, которые:
    - есть в arr2, ИЛИ
    - их перевёрнутая версия есть в arr2
    """
    count = 0
    for x in arr1:
        if x in arr2 or reverse_number(x) in arr2:
            count += 1
    return count