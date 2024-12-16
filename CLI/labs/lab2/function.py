def quick_sort(arr):
    """Швидке сортування"""
    if len(arr) <= 1:
        return  arr  

    pivot = arr[len(arr) // 2]  
    left = [x for x in arr if x < pivot]  
    middle = [x for x in arr if x == pivot]  
    right = [x for x in arr if x > pivot]  

    return quick_sort(left) + middle + quick_sort(right)



def average(list_local):
    """Пошук середнього арифметичного"""
    avg = sum(list_local) / len(list_local)
    return avg

def max_5(list_local):
    """Пошук перших п’яти максимальних елементів"""
    sorted_list = sorted(list_local, reverse=True)[:5]
    return sorted_list

def min_5(list_local):
    """Пошук перших п’яти мінімальних елементів"""
    sorted_list = sorted(list_local)[:5]
    return sorted_list