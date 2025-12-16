def count_subarrays_with_sum(arr, target):
    """
    считает кол-во подмассивов, сумма которых равна target
    подмассив — непрерывная часть массива
    """
    count = 0
    n = len(arr)
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            if current_sum == target:
                count += 1
    return count