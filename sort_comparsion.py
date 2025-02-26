import timeit
import random

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return lst


def merge_sort_bottom_up(array):
    width = 1  # Починаємо з мінімального розміру підмасиву, 2^0 = 1
    length = len(array)
    while width < length:  # Поки розмір підмасиву менший за загальну довжину масиву
        left = 0
        while left < length:  # Проходимо по масиву зліва направо
            right = min(left + (width * 2 - 1), length - 1)  # Визначаємо праву межу для об'єднання
            middle = min(left + width - 1, length - 1)  # Визначаємо середню межу для об'єднання
            merge(array, left, middle, right)  # Злиття двох підмасивів
            left += width * 2  # Переходимо до наступного підмасиву
        width *= 2  # Збільшуємо розмір підмасиву вдвічі на кожній ітерації
    return array  # Повертаємо відсортований масив

def merge(array, left, middle, right):
    n1 = middle - left + 1  # Довжина першого підмасиву
    n2 = right - middle  # Довжина другого підмасиву

    left_array = [0] * n1  # Тимчасовий масив для першого підмасиву
    right_array = [0] * n2  # Тимчасовий масив для другого підмасиву

    # Копіюємо дані в тимчасові масиви
    for i in range(0, n1):
        left_array[i] = array[left + i]
    for i in range(0, n2):
        right_array[i] = array[middle + i + 1]

    i, j, k = 0, 0, left
    # Злиття двох тимчасових масивів у основний масив
    while i < n1 and j < n2:
        if left_array[i] <= right_array[j]:
            array[k] = left_array[i]
            i += 1
        else:
            array[k] = right_array[j]
            j += 1
        k += 1

    # Додавання залишкових елементів з першого та другого підмасивів
    while i < n1:
        array[k] = left_array[i]
        i += 1
        k += 1
    while j < n2:
        array[k] = right_array[j]
        j += 1
        k += 1


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge_recursive(merge_sort(left_half), merge_sort(right_half))

def merge_recursive(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи, 
		# додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged



lists = [
    [5, 3, 8, 4, 2, 1, 7],
    [1, 2, 4, 5, 7, 8, 9],
    [9, 7, 5, 4, 3, 2, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [random.randint(1, 100) for _ in range(300)]
]
n = 100000

for numbers in lists:
    print("List: ", numbers)
    print("Insertion sort: ", timeit.timeit(lambda: insertion_sort(numbers)), n)
    print("Merge iterative sort: ", timeit.timeit(lambda: merge_sort_bottom_up(numbers)), n)
    print("Merge recursive sort: ", timeit.timeit(lambda: merge_sort(numbers)), n)
    print("Timsort: ", timeit.timeit(lambda: sorted(numbers)), n)
    print()
